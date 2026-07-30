-- Last updated: 29/07/2026, 21:34:48
-- Write your PostgreSQL query statement below

select name as Customers
from customers
where id not in (select distinct customerid from orders)
