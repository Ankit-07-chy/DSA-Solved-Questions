# Write your MySQL query statement below
select 
    user_id,
    concat(Upper(substring(name,1,1)), Lower(substring(name,2,length(name)))) as name
from Users
order by user_id;