API_KEY = ""
# A unique API key obtained from OpenWeatherMap service used to authenticate requests
# and access weather data.


WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
# The URL for retrieving current weather data from OpenWeatherMap API.
# It includes placeholders '{}' for the location and API key which will be replaced
# with actual values when making requests.

FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric"
# The URL for retrieving weather forecast data from OpenWeatherMap API.

SECRET_KEY = "secret_key"
# A secret key used for securely signing the session cookie in Flask.

SQLALCHEMY_DATABASE_URI = "sqlite:///users.db"
# The URI for connecting to the SQLite database named "users.db".