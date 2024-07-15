#!/usr/bin/python3
import os

# General Flask settings
DEBUG = True
SECRET_KEY = 'c64a9fc5289651846ff1915dd2ff2bdb4d58f0d7477ce642'

# Database settings
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:gotravel_dev_pwd@localhost/gotravel_dev'
SQLALCHEMY_TRACK_MODIFICATIONS = False
