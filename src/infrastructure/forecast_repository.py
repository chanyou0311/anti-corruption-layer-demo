from domain.forecast import Forecast, Weather
from domain.forecast_repository_interface import ForecastRepositoryInterface
from infrastructure.forecast_adapter import ForecastAdapter


class ForecastRepository(ForecastRepositoryInterface):
    forecast_adapter: ForecastAdapter

    def __init__(self, forecast_adapter: ForecastAdapter):
        self.forecast_adapter = forecast_adapter

    def get(self, city_id: int) -> Forecast:
        forecast = self.forecast_adapter.get(city_id)
        return forecast
