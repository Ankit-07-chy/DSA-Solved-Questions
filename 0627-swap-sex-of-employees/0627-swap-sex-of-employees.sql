# Write your MySQL query statement below
/*
SELECT
    s.id,
    s.name,
    CASE
        WHEN s.sex = 'f' THEN 'm'
        when s.sex = 'm' then 'f'
    END AS sex,
    s.salary
FROM Salary s;
*/
update Salary s set sex=
case 
    when s.sex = 'f' then 'm'
    else 'f'
end;