WITH full_table AS (
    SELECT
        e.name AS Employee,
        d.name AS Department,
        e.salary AS Salary
    FROM Employee e
    JOIN Department d
        ON e.departmentId = d.id
)

SELECT
    ft.Department,
    ft.Employee,
    ft.Salary
FROM full_table ft
WHERE ft.Salary = (
    SELECT MAX(ft2.Salary)
    FROM full_table ft2
    WHERE ft2.Department = ft.Department
);