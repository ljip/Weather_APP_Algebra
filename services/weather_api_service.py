from datetime import datetime, timedelta
from config.config import FORECAST_URL, API_KEY  # Import necessary modules and variables

import requests  # Import the requests module for making HTTP requests

class WeatherApiService:
    def resolve_api_response_one_day(city: str) -> list:
        # Retrieve and parse forecast data for one day from the API response
        forecast_response = requests.get(FORECAST_URL.format(city, API_KEY))  # Send a GET request to the API

        if forecast_response.status_code == 200:  # Check if the response is successful
            forecast_data = forecast_response.json()  # Parse the JSON data from the response
            current_dt_txt = forecast_data["list"][0]["dt_txt"]  # Extract the current date and time from the data
            current_date = datetime.strptime(current_dt_txt, "%Y-%m-%d %H:%M:%S").date()  # Convert the string to a date object
            max_date = current_date + timedelta(days=1)  # Calculate the maximum date for filtering the data
            todays_forecast_data = []  # Initialize an empty list to store the filtered forecast data
            midnight = datetime(2023, 1, 1, 0, 0, 0).time()  # Create a time object representing midnight

            for data in forecast_data["list"]:
                dt_txt = data["dt_txt"]
                date = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").date()
                time = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").time()

                # Filter the data for the current date or the maximum date at midnight
                if date == current_date or (date == max_date and time == midnight):
                    # Extract relevant information from the data and add it to the list
                    temp_min = data["main"]["temp_min"]
                    temp_max = data["main"]["temp_max"]
                    description = data["weather"][0]["description"]
                    icon = data["weather"][0]["icon"]

                    todays_forecast_data.append(
                        {
                            "city": city,
                            "temp_min": temp_min,
                            "temp_max": temp_max,
                            "description": description,
                            "icon": icon,
                            "date": dt_txt[:10],
                            "datetime": dt_txt
                        }
                    )
            return todays_forecast_data


    def get_forecast_data_three_days(city: str) -> list:
        # Retrieve and parse forecast data for three days from the API response
        forecast_response = requests.get(FORECAST_URL.format(city, API_KEY))  # Send a GET request to the API

        if forecast_response.status_code == 200:  # Check if the response is successful
            forecast_data = forecast_response.json()  # Parse the JSON data from the response
            current_dt_txt = forecast_data["list"][0]["dt_txt"]  # Extract the current date and time from the data
            current_date = datetime.strptime(current_dt_txt, "%Y-%m-%d %H:%M:%S").date()  # Convert the string to a date object
            max_date = current_date + timedelta(days=3)  # Calculate the maximum date for filtering the data
            todays_forecast_data = []  # Initialize an empty list to store the filtered forecast data

            for data in forecast_data["list"]:
                dt_txt = data["dt_txt"]
                date = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").date()

                # Filter the data for dates within the next three days


                if date < max_date:
                    # Extract relevant information from the data and add it to the list
                    temp_min = data["main"]["temp_min"]
                    temp_max = data["main"]["temp_max"]
                    description = data["weather"][0]["description"]
                    icon = data["weather"][0]["icon"]

                    todays_forecast_data.append(
                        {
                            "city": city,
                            "temp_min": temp_min,
                            "temp_max": temp_max,
                            "description": description,
                            "icon": icon,
                            "date": dt_txt[:10],
                            "datetime": dt_txt
                        }
                    )
            return todays_forecast_data


    def get_forecast_data_seven_days(city: str) -> list:
        # Retrieve and parse forecast data for seven days from the API response
        forecast_response = requests.get(FORECAST_URL.format(city, API_KEY))  # Send a GET request to the API

        if forecast_response.status_code == 200:  # Check if the response is successful
            forecast_data = forecast_response.json()  # Parse the JSON data from the response
            current_dt_txt = forecast_data["list"][0]["dt_txt"]  # Extract the current date and time from the data
            current_date = datetime.strptime(current_dt_txt, "%Y-%m-%d %H:%M:%S").date()  # Convert the string to a date object
            max_date = current_date + timedelta(days=7)  # Calculate the maximum date for filtering the data
            todays_forecast_data = []  # Initialize an empty list to store the filtered forecast data

            for data in forecast_data["list"]:
                dt_txt = data["dt_txt"]
                date = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").date()

                # Filter the data for dates within the next seven days
                if date < max_date:
                    # Extract relevant information from the data and add it to the list
                    temp_min = data["main"]["temp_min"]
                    temp_max = data["main"]["temp_max"]
                    description = data["weather"][0]["description"]
                    icon = data["weather"][0]["icon"]

                    todays_forecast_data.append(
                        {
                            "city": city,
                            "temp_min": temp_min,
                            "temp_max": temp_max,
                            "description": description,
                            "icon": icon,
                            "date": dt_txt[:10],
                            "datetime": dt_txt
                        }
                    )
            return todays_forecast_data