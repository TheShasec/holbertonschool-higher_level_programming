-- djf
SELECT tv_genres.name FROM tv_genres JOIN ON tv_genres.id = tv_show_genres.genre_id JOIN ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.name = Dexter;
