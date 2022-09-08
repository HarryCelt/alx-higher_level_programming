-- dispalys the max temperature of each sate
-- from Temperatures
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
