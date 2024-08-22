# Write your MySQL query statement below

SELECT ROUND(SUM(tiv_2016), 2) tiv_2016
FROM Insurance
WHERE pid IN (
    SELECT DISTINCT I1.pid
    FROM Insurance I1, Insurance I2
    WHERE I1.tiv_2015 = I2.tiv_2015
    AND I1.pid <> I2.pid)
AND pid NOT IN (
    SELECT DISTINCT I1.pid
    FROM Insurance I1, Insurance I2
    WHERE I1.lat = I2.lat
    AND I1.lon = I2.lon
    AND I1.pid <> I2.pid
)

