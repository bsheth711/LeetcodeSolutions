# Write your MySQL query statement below
SELECT DISTINCT name
FROM SalesPerson
WHERE name NOT IN (
    SELECT SalesPerson.name
    FROM SalesPerson, Company, Orders
    WHERE Orders.sales_id = SalesPerson.sales_id
    AND Orders.com_id = Company.com_id
    AND Company.name = "RED"
)