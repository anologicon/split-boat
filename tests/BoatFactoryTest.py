import unittest

from src.factories.BoatFactory import BoatFactory


class BoatFactoryTest(unittest.TestCase):

    def test_shouldCreateANewBoat(self):

        boat_factory = BoatFactory()

        boat = boat_factory.create(plate='AV34AG6')

        self.assertEqual('AV34AG6', boat.plate)


if __name__ == '__main__':
    unittest.main()
