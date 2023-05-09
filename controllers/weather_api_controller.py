from services.weather_api_service import WeatherApiService


class WeatherApiController:
    def get_forecast_data_one_day(city: str) -> list:
        return WeatherApiService.resolve_api_response_one_day(city)
    
    
    def get_forecast_data_three_days(city: str) -> list:
        return WeatherApiService.get_forecast_data_three_days(city)
    
    
    def get_forecast_data_seven_days(city: str) -> list:
        return WeatherApiService.get_forecast_data_seven_days(city)