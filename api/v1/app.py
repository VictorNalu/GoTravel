# api/v1/app.py
from flask import Flask, jsonify, make_response, render_template
from flask_cors import CORS
from flasgger import Swagger
from models import storage
from werkzeug.exceptions import HTTPException
import os

# Import the blueprint after creating it
from api.v1.views import app_views

# Global Flask Application Variable: app
app = Flask(__name__, template_folder='../../templates', static_folder='../../static', static_url_path='/static')
swagger = Swagger(app)

# Global strict slashes
app.url_map.strict_slashes = False

# Flask server environmental setup
host = os.getenv('GOTRAVEL_API_HOST', '0.0.0.0')
port = os.getenv('GOTRAVEL_API_PORT', 5000)

# Cross-Origin Resource Sharing
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Register the blueprint before any route definition
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    """
    After each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()

@app.errorhandler(404)
def handle_404(exception):
    """
    Handles 404 errors
    """
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), 404)

@app.errorhandler(400)
def handle_400(exception):
    """
    Handles 400 errors
    """
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), 400)

@app.errorhandler(Exception)
def global_error_handler(err):
    """
    Global route to handle all error status codes
    """
    if isinstance(err, HTTPException):
        if type(err).__name__ == 'NotFound':
            err.description = "Not found"
        message = {'error': err.description}
        code = err.code
    else:
        message = {'error': str(err)}
        code = 500
    return make_response(jsonify(message), code)

def setup_global_errors():
    """
    This updates HTTPException class with custom error function
    """
    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, global_error_handler)
@app.route('/')
def root_home():
    """route for root home page"""
    return render_template('index.html')

def create_app():
    app.config.from_pyfile('config.py')
    return app

if __name__ == "__main__":
    """
    MAIN Flask App
    """
    # Initializes global error handling
    setup_global_errors()
    # Start Flask app
    app.run(host=host, port=port, debug=True)
