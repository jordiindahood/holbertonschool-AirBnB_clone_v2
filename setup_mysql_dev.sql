-- script that creates the database hbtn_0c_0
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE  hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
