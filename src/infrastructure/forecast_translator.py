from typing import Optional

from domain.forecast import Forecast, Weather


class ForecastTranslator:
    base_url = "http://weather.livedoor.com/forecast/webservice/json/v1"

    def convert_to_forecast_from_data(self, data: dict) -> Forecast:
        today_weather = self.__get_today_weather(data)
        tomorrow_weather = self.__get_tomorrow_weather(data)
        prefecture = data["location"]["prefecture"]
        city = data["location"]["city"]
        return Forecast(
            today=today_weather,
            tomorrow=tomorrow_weather,
            prefecture=prefecture,
            city=city,
        )

    def __get_today_weather(self, data: dict) -> Optional[Weather]:
        forecasts = data["forecasts"]
        for forecast in forecasts:
            if forecast["dateLabel"] == "今日":
                if forecast["temperature"]["max"] is None:
                    return None
                max_temperature=forecast["temperature"]["max"]["celsius"]
                min_temperature=forecast["temperature"]["min"]["celsius"]
                telop=forecast["telop"]
                return Weather(max_temperature, min_temperature, telop)
        raise ValueError

    def __get_tomorrow_weather(self, data: dict) -> Optional[Weather]:
        forecasts = data["forecasts"]
        for forecast in forecasts:
            if forecast["dateLabel"] == "明日":
                if forecast["temperature"]["max"] is None:
                    return None
                max_temperature=forecast["temperature"]["max"]["celsius"]
                min_temperature=forecast["temperature"]["min"]["celsius"]
                telop=forecast["telop"]
                return Weather(max_temperature, min_temperature, telop)
        raise ValueError
