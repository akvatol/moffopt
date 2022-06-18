from parser import Parser


class ChildParser(Parser):

    def _get_content(self, _):
        """Mock"""

    def _parse_x(self, _) -> str:
        return "a"

    def _parse_y(self, _) -> str:
        return "b"

    def _parse_parse_(self, _) -> str:
        return "c"

    def _parse__parse_(self, _) -> str:
        return "d"


def test_parser():

    assert ChildParser().parse("...") == {
        "x": "a", "y": "b",
        "parse_": "c", "_parse_": "d"
    }
