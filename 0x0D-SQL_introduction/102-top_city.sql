-- displays the top 3 of cities temperature
-- during July and August ordered by temeperature
SELECT city, AVG(value) AS avg_temp FROM temepratures WHERE MONTH= 7 OR MONTH= 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
