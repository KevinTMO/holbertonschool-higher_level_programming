-- Lists all genres from hbtn_0d_tvshows and display the number of shows linked to each
-- Each record like: <TV show genre> - <Number of shows linked to this genre>
-- Firs column will be called "genre"
-- Second column should be called "number_of_shows"
-- Don't display a genre that doesn't have any shows linked
-- Results must be sorted in desceding order by number of shows linked
-- Only on SELECT

SELECT tv_genres.name AS genre, COUNT(*) AS "number_of_shows"
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
