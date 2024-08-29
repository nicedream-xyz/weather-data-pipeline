CREATE DATABASE weather_db;
USE weather_db;

CREATE TABLE weather_observations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    station_id VARCHAR(10),
    station_name VARCHAR(100),
    station_timezone VARCHAR(50),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    observation_timestamp DATETIME,
    temperature DECIMAL(5,2),
    wind_speed DECIMAL(5,2),
    humidity DECIMAL(5,2),
    UNIQUE (station_id, observation_timestamp)
);
