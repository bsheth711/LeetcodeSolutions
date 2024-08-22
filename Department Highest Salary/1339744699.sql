# Write your MySQL query statement below
SELECT R.depName Department, R.empName Employee, R.salary Salary
FROM (
SELECT E.salary, E.name empName, D.name depName, DENSE_RANK() OVER (PARTITION BY E.departmentId ORDER BY E.salary DESC) ranked
FROM Employee E
LEFT JOIN Department D ON E.departmentId = D.id
) R
WHERE R.ranked = 1