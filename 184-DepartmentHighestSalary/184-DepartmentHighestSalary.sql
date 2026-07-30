-- Last updated: 29/07/2026, 22:39:34
-- Write your PostgreSQL query statement below

with joined as 
(select e.name as Employee, e.salary as Salary, d.name as Department
from employee e
join department d
on e.departmentid=d.id)

select Department, Employee, Salary from (
select Department, Employee, Salary,
rank() over (partition by Department order by salary desc) as salary_rank
from joined)
where salary_rank =1


