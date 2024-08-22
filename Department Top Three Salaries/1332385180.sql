# Write your MySQL query statement below
WITH HighestSalary AS (
    SELECT MAX(salary) salary, departmentId
    FROM Employee
    GROUP BY departmentId
),
SecondHighestSalary AS (
    SELECT MAX(E.salary) salary, E.departmentId
    FROM Employee E
    LEFT JOIN HighestSalary E2 ON E.departmentId = E2.departmentId
    WHERE E.salary < E2.salary
    GROUP BY E.departmentId
),
ThirdHighestSalary AS (
    SELECT MAX(E.salary) salary, E.departmentId
    FROM Employee E
    LEFT JOIN SecondHighestSalary E2 ON E.departmentId = E2.departmentId
    WHERE E.salary < E2.salary
    GROUP BY E.departmentId
)
SELECT D.name Department, E.name Employee, E.salary Salary
FROM Employee E
LEFT JOIN HighestSalary E2 ON E.departmentId = E2.departmentId
LEFT JOIN SecondHighestSalary E3 ON E.departmentId = E3.departmentId
LEFT JOIN ThirdHighestSalary E4 ON E.departmentId = E4.departmentId
LEFT JOIN Department D ON E.departmentId = D.id
WHERE E.salary = E2.salary 
OR E.salary = E3.salary
OR E.salary = E4.salary

/*
SELECT
FROM Employee E
LEFT JOIN ThirdHighestSalary E2 ON E.departmentId = 
WHERE E.salary >= ThirdHighestSalary.salary
*/
