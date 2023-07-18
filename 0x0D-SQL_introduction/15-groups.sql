-- lists the number of records with the same score from second_table
-- results should display the score, number of records
-- The list should be sorted by the number of records (descending)

SELECT score, COUNT(*)
as number FROM second_table
GROUP BY score ORDER BY number DESC;
