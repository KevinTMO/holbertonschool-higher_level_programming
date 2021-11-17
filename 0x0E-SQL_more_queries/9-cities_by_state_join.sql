-- Lists all cities contained in the database
-- Each record should display: cities.ID - cities.NAME - states.NAME
-- Results must be sorted in ascending order by cities.ID
-- You can only use ONE SELECT STATEMENT

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
