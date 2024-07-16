#!/bin/env bash

# Check if MySQL is enabled and start it if it is not
    if service mysql status | grep -q "active (running)"; then
    echo "MySQL is already running."
else
    echo "MySQL is not running. Starting MySQL..."
    sudo service mysql start
fi

# Set the PYTHONPATH environment variable to include the current directory and the api directory
export PYTHONPATH=$(pwd):$(pwd)/api

# Set the storage type to 'db'
export GOTRAVEL_TYPE_STORAGE=db

# Set the MySQL username for the GoTravel application
export GOTRAVEL_MYSQL_USER=gotravel_dev

# Set the MySQL password for the GoTravel application
export GOTRAVEL_MYSQL_PWD=gotravel_dev_pwd

# Set the MySQL host for the GoTravel application
export GOTRAVEL_MYSQL_HOST=localhost

# Set the MySQL database name for the GoTravel application
export GOTRAVEL_MYSQL_DB=gotravel_dev_db

# Set the FLASK_APP environment variable to point to the create_app function in the api.v1.app module
export FLASK_APP="api.v1.app:create_app()"

# Print the value of the FLASK_APP environment variable to the terminal
echo $FLASK_APP
flask run
