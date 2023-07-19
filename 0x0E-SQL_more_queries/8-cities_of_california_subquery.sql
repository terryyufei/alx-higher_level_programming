-- lists all the cities of california in database hbtn_0d_usa
-- states table conatins only one record where name= california, id can be difffrent
-- not allowed to use the JOIN keyword

SELECT id, name
FROM hbtn_0d_usa.cities
WHERE state_id = (
    SELECT id
    FROM hbtn_0d_usa.states
    WHERE name = 'california'
)
ORDER BY id ASC;
