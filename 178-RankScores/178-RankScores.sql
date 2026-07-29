-- Last updated: 28/07/2026, 23:04:52
-- Write your PostgreSQL query statement below
select score,
dense_rank() over (order by score desc) as rank
from scores
