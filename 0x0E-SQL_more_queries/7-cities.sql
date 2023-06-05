-- Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXSIST hbtn_0d_usa;
USE hbtn_0d_usa
CREATE TABLE IF NOT EXSIST cities, (id INT UNIQUE NOT NULL AUTO_INCREMENT,
state_id NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY_KEY (id)
FOREIGN_KEY (state_id) REFERENCES states (id))