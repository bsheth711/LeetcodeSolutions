# Write your MySQL query statement below
WITH Res AS (
    SELECT id, name
    FROM Customers
    EXCEPT
    SELECT Orders.customerId, Customers.name
    FROM Orders
    LEFT JOIN Customers
    ON Customers.id = Orders.customerId
    GROUP BY customerId
)
SELECT name AS Customers FROM Res