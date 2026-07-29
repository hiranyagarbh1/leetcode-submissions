-- Last updated: 29/07/2026, 11:55:09
-- Write your PostgreSQL query statement below

with self_join as 
(select e.name as Employee, e.salary as empsal, m.name as mname, m.salary as msal
from employee e
join employee m
on m.id=e.managerid
where e.salary > m.salary)

select Employee
from self_join


