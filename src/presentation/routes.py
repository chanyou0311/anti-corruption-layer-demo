from dataclasses import asdict

import responder
import requests

from application.forecast_service import ForecastService
from infrastructure.forecast_repository import ForecastRepository
from infrastructure.forecast_adapter import ForecastAdapter
from infrastructure.forecast_client import ForecastClient
from infrastructure.forecast_translator import ForecastTranslator


FORECAST_BASE_URL = "http://weather.livedoor.com/forecast/webservice/json/v1"

api = responder.API()


@api.route("/")
async def health(req, resp):
    resp.media = {"status": "ok"}


@api.route("/forecast/{city_id}")
async def get_forecast_from_city_id(req, resp, *, city_id):
    forecast_repository = ForecastRepository(
        ForecastAdapter(
            ForecastClient(),
            ForecastTranslator()
        )
    )
    forecast_service = ForecastService(forecast_repository)
    forecast = forecast_service.get_forecast_from_city_id(city_id)
    resp.media = asdict(forecast)
