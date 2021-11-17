-- Creates a table unique_id with:
-- id INT = 1 but must be UNIQUE
-- name VARCHAR(256)

CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
