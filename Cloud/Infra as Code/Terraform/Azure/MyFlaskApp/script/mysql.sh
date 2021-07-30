#!/bin/bash

sudo mysql -uroot -e "CREATE DATABASE myflaskapp;"
sudo mysql -uroot -e "SELECT User,Host FROM mysql.user;"
sudo mysql -uroot -e "CREATE USER 'daniel'@'localhost' IDENTIFIED BY '324DanS';"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON myflaskapp.* TO 'daniel'@'localhost';"
sudo mysql -uroot -e "USE myflaskapp; CREATE TABLE users(id INT(11) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR (100), username VARCHAR(30), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
sudo mysql -uroot -e "USE myflaskapp; CREATE TABLE isp_templates (id INT(11) AUTO_INCREMENT PRIMARY KEY, isp VARCHAR(50), type VARCHAR(50), model VARCHAR(50), site VARCHAR(15), ci_name VARCHAR(50), config longtext, last_editor VARCHAR(100), create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"


