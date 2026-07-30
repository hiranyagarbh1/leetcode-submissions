-- Last updated: 29/07/2026, 21:36:10
-- Write your PostgreSQL query statement below

select email
from person
group by email
having count(email) > 1
