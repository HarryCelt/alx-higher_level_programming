-- displays the top 3 of cities temperature
-- during July and August ordered by temeperature in descending order
-- from the table Temperatures
SELECT city, AVG(value) AS avg_temp
FROM temepratures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
