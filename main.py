# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.factories.BoatFactory import BoatFactory

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    boatFactory = BoatFactory()

    boat = boatFactory.create('AJGAEJWoia')

    print(f"Barco {boat.plate}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
