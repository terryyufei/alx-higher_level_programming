-- creates the table id_not_null
-- description id(INT) and NOT NULL with default value 1
-- name VARCHAR(256)
-- If the table id_not_null already exists, your script should not fail

CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);
