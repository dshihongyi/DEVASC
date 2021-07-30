#!/bin/bash
sudo git init
sudo git clone https://github.com/dshihongyi/Flask-Dev.git
cd Flask-Dev
sudo apt-get update 
sudo apt-get -y upgrade
sudo apt-get -y install python3-pip
sudo apt-get -y install mysql-server libmysqlclient-dev
sudo pip3 install -r requirements.txt
sudo mysql -u root

SELECT User,Host FROM mysql.user;
CREATE USER 'daniel'@'localhost' IDENTIFIED BY '324DanS';
GRANT ALL PRIVILEGES ON myflaskapp.* TO 'daniel'@'localhost';
CREATE DATABASE myflaskapp;
USE myflaskapp;
CREATE TABLE users(id INT(11) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR (100), username VARCHAR(30), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE isp_templates (id INT(11) AUTO_INCREMENT PRIMARY KEY, isp VARCHAR(50), type VARCHAR(50), model VARCHAR(50), site VARCHAR(15), ci_name VARCHAR(50), config longtext, last_editor VARCHAR(100), create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
exit
