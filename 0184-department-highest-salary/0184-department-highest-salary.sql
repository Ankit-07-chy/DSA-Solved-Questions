with new_table as (
    select 
        e.salary, d.id
    from Employee e
    join Department d
    on e.departmentId = d.id
),

max_sal_dep_wise as (
    select id,max(salary) as salary
    from new_table
    group by id
)

select 
    d.name as Department,
    e.name as Employee,
    e.salary as Salary
from Employee e
join Department d
on e.departmentId = d.id
join max_sal_dep_wise as m
on m.id = d.id and m.Salary = e.salary;