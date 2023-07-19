-- list all shows without a genre linked
-- sort in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- You can use only one SELECT statement

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
