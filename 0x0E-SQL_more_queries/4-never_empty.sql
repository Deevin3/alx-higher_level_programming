-- Write a script that creates the table id_not_null on your MySQL server.
CREATE TABLE IF NOT EXSIST 'id_not_null';
id INT DEFAULT 1 NOT NULL;
name VARCHAR(256);