-- select distinct v.viewer_id as id
-- from Views v 
-- group by v.viewer_id, v.view_date
-- having count(v.article_id)>1
-- order by id;

with new_table as (
   select * 
      from Views v 
      where v.viewer_id <> v.author_id
)
select distinct nt.viewer_id as id 
   from new_table nt 
   group by nt.viewer_id, nt.view_date
   having count(nt.article_id)>1
   order by id ;