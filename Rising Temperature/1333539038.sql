# Write your MySQL query statement below
SELECT W.id
FROM (
    SELECT id, recordDate, temperature, LAG(temperature) OVER(ORDER BY recordDate ASC) AS yesterdayTemp, LAG(recordDate) OVER(ORDER BY recordDate ASC) AS yesterdayDate
    FROM Weather) W
WHERE W.temperature > W.yesterdayTemp AND DATE_ADD(W.yesterdayDate, INTERVAL 1 DAY) = W.recordDate