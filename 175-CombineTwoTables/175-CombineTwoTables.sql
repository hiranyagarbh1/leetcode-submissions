-- Last updated: 28/07/2026, 22:16:18
-- Write your PostgreSQL query statement below
select p.firstName, p.lastName, a.city, a.state
from Person p
left join Address a
on p.personID=a.personID

