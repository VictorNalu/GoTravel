#!/usr/bin/python3
import os

# General Flask settings
DEBUG = True
SECRET_KEY = 'cdd754e6523f713e48fd617055c732b1a57f48af72bea65e'

# Database settings
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:gotravel_dev_pwd@localhost/gotravel_dev'
SQLALCHEMY_TRACK_MODIFICATIONS = False
