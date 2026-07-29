-- Last updated: 28/07/2026, 23:04:49
-- Write your PostgreSQL query statement below

select
    sell_date,
    count(distinct product) as num_sold,
    string_agg(distinct product, ',' order by product) as products
from Activities
group by sell_date
order by sell_date