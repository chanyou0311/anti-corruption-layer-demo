from abc import ABCMeta, abstractmethod

from .forecast import Forecast


class ForecastRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def get(self, city_id: int) -> Forecast:
        raise NotImplementedError()
