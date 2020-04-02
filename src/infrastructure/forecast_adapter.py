from domain.forecast import Forecast
from infrastructure.forecast_client import ForecastClient
from infrastructure.forecast_translator import ForecastTranslator


class ForecastAdapter():
    forecast_client: ForecastClient
    forecast_translator: ForecastTranslator

    def __init__(self, forecast_client: ForecastClient, forecast_translator: ForecastTranslator):
        self.forecast_client = forecast_client
        self.forecast_translator = forecast_translator

    def get(self, city_id: int)-> Forecast:
        data = self.forecast_client.get(city_id)
        forecast = self.forecast_translator.convert_to_forecast_from_data(data)
        return forecast
