import requests
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# API and database configuration
API_BASE_URL = "https://api.weather.gov"
STATION_ID = "0112W"  
DB_CONFIG = {
    'user': 'root',
    'password': 'Yeezy1298.',
    'host': 'localhost',
    'database': 'weather_db'
}

# Function to obtain station data
def get_station_data(station_id):
    try:
        station_url = f"{API_BASE_URL}/stations/{station_id}"
        response = requests.get(station_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error obtaining data from the station: {e}")
        return None

# Function to obtain station observations
def get_observations(station_id):
    try:
        observations_url = f"{API_BASE_URL}/stations/{station_id}/observations"
        response = requests.get(observations_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error when obtaining observations: {e}")
        return None

# Function to insert data in MySQL
def insert_weather_data(station_data, observations):
    if not station_data or not observations:
        print("No data to insert")
        return

    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        for observation in observations.get('features', []):
            data = observation.get('properties', {})
            station_id = station_data['properties']['stationIdentifier']
            station_name = station_data['properties']['name']
            station_timezone = station_data['properties']['timeZone']
            latitude = station_data['geometry']['coordinates'][1]
            longitude = station_data['geometry']['coordinates'][0]
            observation_timestamp = datetime.fromisoformat(data.get('timestamp', '').replace('Z', '+00:00'))
            temperature = data.get('temperature', {}).get('value')
            wind_speed = data.get('windSpeed', {}).get('value')
            humidity = data.get('relativeHumidity', {}).get('value')

            # Round only if the value is not None
            temperature = round(temperature, 2) if temperature is not None else None
            wind_speed = round(wind_speed, 2) if wind_speed is not None else None
            humidity = round(humidity, 2) if humidity is not None else None

            query = """
            INSERT INTO weather_observations 
            (station_id, station_name, station_timezone, latitude, longitude, 
            observation_timestamp, temperature, wind_speed, humidity)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            temperature = VALUES(temperature),
            wind_speed = VALUES(wind_speed),
            humidity = VALUES(humidity);
            """
            cursor.execute(query, (station_id, station_name, station_timezone, latitude, longitude,
                                   observation_timestamp, temperature, wind_speed, humidity))

        connection.commit()
    except Error as err:
        print(f"Database error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Obtaining and storing data
station_data = get_station_data(STATION_ID)
observations = get_observations(STATION_ID)
insert_weather_data(station_data, observations)
 n
