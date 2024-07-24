# api/v1/views/index.py
from api.v1.views import app_views
from flask import render_template

@app_views.route('/forgot_password')
def forgot_password():
    """defines route for forgotten passwd"""
    return render_template('forgot_password.html')
