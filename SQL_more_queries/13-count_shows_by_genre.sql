-- fdssd
SELECT tv_genres.name , COUNT(*) AS number_of_shows FROM tv_show_genres GROUP BY tv_show_genres.genre_id JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id;
