-- lists all shows without the genre comedy
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement

SELECT title
FROM tv_shows
WHERE title NOT IN (
    SELECT title
    FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
  )
GROUP BY title
ORDER BY title ASC;
