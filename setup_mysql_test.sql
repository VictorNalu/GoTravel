-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS gotravel_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'gotravel_test_pwd';
GRANT ALL PRIVILEGES ON `gotravel_test_db`.* TO 'gotravel_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'gotravel_test'@'localhost';
FLUSH PRIVILEGES;
