-- Last updated: 29/07/2026, 21:49:02
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    WITH ranked AS (
        SELECT e.Salary as sal, DENSE_RANK() OVER (ORDER BY e.Salary DESC) AS salary_rank
        FROM Employee e
    )
    SELECT DISTINCT sal
    FROM ranked
    WHERE salary_rank = N);
END;
$$ LANGUAGE plpgsql;