from src.factories.BoatFactoryInterface import BoatFactoryInterface
from src.models.BoatModel import BoatModel


class BoatFactory(BoatFactoryInterface):

    def create(self, plate: str) -> BoatModel:
        return BoatModel(plate=plate)
