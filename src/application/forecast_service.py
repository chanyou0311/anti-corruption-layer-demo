from domain.forecast import Forecast
from infrastructure.forecast_repository import ForecastRepository


class ForecastService:
    forecast_repository: ForecastRepository

    def __init__(self, forecast_repository: ForecastRepository):
        self.forecast_repository = forecast_repository

    def get_forecast_from_city_id(self, city_id: int) -> Forecast:
        forecast = self.forecast_repository.get(city_id)
        return forecast
