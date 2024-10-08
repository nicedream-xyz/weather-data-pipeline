# Weather Data Pipeline

## Project Description
This project implements a data pipeline that retrieves, stores, and analyzes weather information from a specific station (`0112W`) using the National Weather Service public API. The data is stored in a MySQL database.

## Project Structure
- `src/pipeline.py`: Main script that executes the data pipeline.
- `db/create_table.sql`: Script to create the `weather_observations` table in MySQL.
- `db/query_data.sql` : Script to query the required data.
- `requirements.txt`: File containing the necessary Python dependencies.

## Requirements
- Python 3.12
- MySQL Server
- Python Libraries: `requests`, `mysql-connector-python`

## Installation

### Clone the Repository

```bash
git clone https://github.com/nicedream-xyz/weather-data-pipeline.git
cd weather-data-pipeline
