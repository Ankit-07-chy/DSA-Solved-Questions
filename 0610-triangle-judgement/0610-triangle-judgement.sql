# Write your MySQL query statement below

select 
    t.x, t.y, t.z, 
    case 
        when t.x + t.y <= t.z or t.y + t.z <= t.x or t.z + t.x <= t.y then 'No' else 'Yes' 
        end as triangle

from Triangle t;