import requests


class ForecastClient:
    base_url = "http://weather.livedoor.com/forecast/webservice/json/v1"

    def get(self, city_id: int) -> dict:
        response = requests.get(self.base_url, params={"city": city_id})
        if response.status_code != 200:
            error = {"error": "invalid city_id", "status_code": response.status_code}
            raise Exception(error)
        return response.json()
