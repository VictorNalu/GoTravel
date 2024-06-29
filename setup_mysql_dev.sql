-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS gotravel_dev_db;
CREATE USER IF NOT EXISTS 'gotravel_dev'@'localhost' IDENTIFIED BY 'gotravel_dev_pwd';
GRANT ALL PRIVILEGES ON `gotravel_dev_db`.* TO 'gotravel_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'gotravel_dev'@'localhost';
FLUSH PRIVILEGES;
