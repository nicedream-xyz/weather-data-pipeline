---Average observed temperature for last week(Mon-Sun).
SELECT AVG(temperature) AS avg_temperature
FROM weather_observations
WHERE observation_timestamp >= DATE_SUB(CURDATE(), INTERVAL 7 DAY);


---Maximum wind speed change between two consecutive observations in the last 7 days.
SELECT MAX(wind_speed_diff) AS max_wind_speed_change
FROM (
    SELECT ABS(wind_speed - LAG(wind_speed) OVER (ORDER BY observation_timestamp)) AS wind_speed_diff
    FROM weather_observations
    WHERE observation_timestamp >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
) AS subquery;
