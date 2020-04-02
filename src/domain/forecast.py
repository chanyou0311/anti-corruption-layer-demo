from typing import Optional

from dataclasses import dataclass


@dataclass
class Weather:
    max_temperature: int
    min_temperature: int
    telop: str


@dataclass
class Forecast:
    today: Optional[Weather]
    tomorrow: Optional[Weather]
    prefecture: str
    city: str
