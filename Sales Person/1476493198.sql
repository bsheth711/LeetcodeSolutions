# Write your MySQL query statement below
SELECT DISTINCT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT Orders.sales_id
    FROM Company, Orders
    WHERE Orders.com_id = Company.com_id
    AND Company.name = "RED"
)