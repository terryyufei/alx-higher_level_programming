-- creates the database hbtn_0d_usa and tables city
-- cities description: id(INT) can't be null, auto generated, primary key
-- state_id must be a foreign key ref to id of the states table
-- name VARCHAR(256) can't be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT, 
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id),
    name VARCHAR(256) NOT NULL
);
