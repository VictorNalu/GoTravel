from flask import Flask, request, jsonify, render_template
from models.engine import db_storage
from models.user import User

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = storage.get_user_by_email(data['email'])
    if user and user.check_password(data['password']):
        return jsonify({"success": True})
    return jsonify({"success": False, "message": "Invalid email or password"})

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if storage.get_user_by_email(data['email']):
        return jsonify({"success": False, "message": "Email already exists"})
    new_user = User(email=data['email'])
    new_user.set_password(data['password'])
    storage.new(new_user)
    storage.save()
    return jsonify({"success": True})

@app.route('/recommendations')
def recommendations():
    # Assuming you have a function to get recommendations from your database
    recs = storage.get_recommendations()
    return jsonify([rec.to_dict() for rec in recs])

@app.route('/most-visited-places')
def most_visited_places():
    # Assuming you have a function to get most visited places from your database
    places = storage.get_most_visited_places()
    return jsonify([place.to_dict() for place in places])

@app.route('/festivals')
def festivals():
    # Assuming you have a function to get festivals from your database
    fests = storage.get_festivals()
    return jsonify([fest.to_dict() for fest in fests])

if __name__ == '__main__':
    app.run(debug=True)
