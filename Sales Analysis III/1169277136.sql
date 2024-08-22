# Write your MySQL query statement below

SELECT Product.product_id, Product.Product_name
FROM Sales, Product
WHERE Sales.product_id = Product.product_id
GROUP BY Sales.product_id
HAVING MIN(Sales.sale_date) >= CAST('2019-01-01' AS DATE)
    AND MAX(Sales.sale_date) <= CAST('2019-03-31' AS DATE)