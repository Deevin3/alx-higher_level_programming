-- Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXSIST hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLR IF NOT EXSIST states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256), NOT null PRIMARY_KEY (id))