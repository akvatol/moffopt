from pathlib import Path
from tempfile import NamedTemporaryFile
from json import dump


from parser import DemoParserCoordinates

MODE_WRITE_TEXT = "w+t"


def test_coordinates():
    data = {"x": 1, "y": 2, "z": 3}

    with NamedTemporaryFile(MODE_WRITE_TEXT) as file:
        dump(obj=data, fp=file)
        file.seek(0)  # TODO: How it works?

        filepath = Path(file.name)
        coordinates = DemoParserCoordinates(filepath)

        assert coordinates.x == 1
        assert coordinates.y == 2
        assert coordinates.z == 3
