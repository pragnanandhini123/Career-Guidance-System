CREATE DATABASE career_db;
USE career_db;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marks FLOAT,
    skills FLOAT,
    interest FLOAT,
    prediction VARCHAR(100)
);
