from pathlib import Path
from json import load


class DemoParserCoordinates:

    def __init__(self, filepath: Path):
        self.__filepath = filepath

    @property
    def x(self) -> float:
        return self.__parse()["x"]

    @property
    def y(self) -> float:
        return self.__parse()["y"]

    @property
    def z(self) -> float:
        return self.__parse()["z"]

    def __parse(self) -> dict:
        with open(self.__filepath) as file:
            return load(file)
