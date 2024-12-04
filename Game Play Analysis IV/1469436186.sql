# Write your MySQL query statement below
WITH Data AS (
    SELECT DENSE_RANK() OVER (w) AS login_number,
        LAG(event_date) OVER (w) AS last_login,
        player_id, event_date
    FROM Activity
    WINDOW w AS (PARTITION BY player_id ORDER BY event_date)
), PlayerNumber AS (
    SELECT COUNT(DISTINCT player_id) AS players
    FROM Activity
)
SELECT IFNULL(ROUND(COUNT(Data.player_id) / PlayerNumber.players, 2), 0) AS fraction
FROM Data, PlayerNumber
WHERE Data.login_number = 2 AND Data.event_date = DATE_ADD(Data.last_login, INTERVAL 1 DAY)
