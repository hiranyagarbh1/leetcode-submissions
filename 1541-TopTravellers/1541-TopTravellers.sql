-- Last updated: 28/07/2026, 22:46:36
-- Write your PostgreSQL query statement below

with grouped as
(select u.id, u.name, r.distance
from users u
left join rides r
on u.id=r.user_id)

select name, sum(coalesce(distance,0)) as travelled_distance
from grouped
group by id, name
order by travelled_distance desc, name asc