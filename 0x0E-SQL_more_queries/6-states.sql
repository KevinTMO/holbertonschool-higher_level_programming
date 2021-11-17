-- Create a database hbtn_0d_usa and the table state
-- States table will get id INT and name VARCHAR(256) -> Cant be null
-- If database and table exists just ignore

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
       id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR(256) NOT NULL
);
