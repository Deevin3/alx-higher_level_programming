-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT title
FROM tv_title
LEFT JOIN tv_show_genre ON tv_show_genre.id = tv_show_genre.genre_id
LEFT JOIN tv_show_genre ON tv_show_genre.genre_id = tv_show.id
WHERE tv_genre.name = 'Comedy'
GROUP BY title
ORDER BY title ASC;