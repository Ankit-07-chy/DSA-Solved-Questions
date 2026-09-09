# Write your MySQL query statement below

select
    e2.name
from Employee e1
join Employee e2
on e1.managerid = e2.id
group by e1.managerid,e2.name
having count(e2.department) >=5;