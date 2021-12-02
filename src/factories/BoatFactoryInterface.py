from abc import ABC, abstractmethod

from src.models.BoatModel import BoatModel


class BoatFactoryInterface(ABC):

    @abstractmethod
    def create(self, plate: str) -> BoatModel:
        """ Create a new Boat object with plate"""
