# Write your MySQL query statement below

-- name of user who rated gretest number of movies
-- find movie name wihth highest avg rating in feb 2020

(select
    u.name as results
from MovieRating mr 
left join Users u 
    on mr.user_id = u.user_id
group by mr.user_id
order by count(1) desc, u.name

limit 1)

union all

(
select 
    m.title as results
from MovieRating mr
left join Movies m
    on mr.movie_id = m.movie_id
where mr.created_at like '2020-02%'
group by mr.movie_id
order by avg(mr.rating) desc, m.title
limit 1)
;