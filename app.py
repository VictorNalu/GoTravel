import logging
from flask import Flask, render_template

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
app.logger.info('Starting Flask app...')

@app.route('/')
def landing_page():
    app.logger.info('Serving landing page...')
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
