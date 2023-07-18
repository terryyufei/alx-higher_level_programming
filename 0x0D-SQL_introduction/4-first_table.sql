-- creates a table called first_table in the current DB in my MySQL server
-- If the table first_table already exists, your script should not fail
-- You are not allowed to use the SELECT or SHOW statements
-- attributes include id and name

CREATE TABLE IF NOT EXISTS first_table(
    id INT,
    name VARCHAR(256)
);
