-- Question:
-- Show all employees with duplicate salaries

SELECT salary, COUNT(*)
FROM employee
GROUP BY salary
HAVING COUNT(*) > 1;
