-- Last updated: 28/07/2026, 23:04:48
-- Write your PostgreSQL query statement below

with numbered as (
    select
        num,
        id,
        lead(num, 1) over (order by id) as next1,
        lead(num, 2) over (order by id) as next2
    from logs
)
select distinct num as ConsecutiveNums
from numbered
where num = next1 and num = next2
