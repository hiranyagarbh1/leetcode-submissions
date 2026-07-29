-- Last updated: 28/07/2026, 22:16:20
-- Write your PostgreSQL query statement below
-- select
-- (select distinct salary
-- from employee
-- order by salary desc
-- limit 1 offset 1) as secondhighestsalary

with ranked as (
    select salary,
           dense_rank() over (order by salary desc) as salary_rank
    from Employee
)

select (
    select distinct salary
    from ranked
    where salary_rank = 2
) as SecondHighestSalary