# Write your MySQL query statement below
with new_table as (
select 
    a1.machine_id, a1.process_id ,a2.timestamp-a1.timestamp as diff
from activity a1
join activity a2 
on a1.machine_id = a2.machine_id and a1.process_id = a2.process_id and a1.activity_type ='start' and a2.activity_type = 'end'
)

select 
    machine_id, round(sum(diff)/count(*),3) as processing_time

from new_table
group by machine_id