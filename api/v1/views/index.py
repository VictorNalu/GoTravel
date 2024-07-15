# api/v1/views/index.py
from api.v1.views import app_views
from flask import render_template

@app_views.route('/')
def home():
    """Route for home page"""
    return render_template('index.html')
