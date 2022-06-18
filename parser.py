from typing import Any, Tuple


class Parser:
    """
    Provides `parser` method which executes all methods started from `_parse_`
    and returns `dict` where:
    * key is `_parse_method` name without `_parse_`
    * value is `_parse_method` result

    For example:
    ```
    class pKaParser(Parser):
        def _parse_pKa(self, content: str) -> str:
            return "1.0"

    pka = pKaParser().parse(filepath)  # pka = {"pKa": "1.0"}
    ```
    """

    _KEYWORLD_PARSE = "_parse_"
    _PLACEHOLDER_EMPTY = ""
    _FIRST_ENTRY = 1

    def parse(self, filepath: str) -> dict:
        content = self._get_content(filepath)
        return dict(
            self._get_parsed_name_value_pair(method_name, content)
            for method_name in dir(self) if self._is_parse_method(method_name)
        )

    def _get_content(self, filepath) -> str:
        with open(filepath) as file:
            return file.read()

    def _is_parse_method(self, method_name: str) -> bool:
        return method_name.startswith(self._KEYWORLD_PARSE)

    def _get_parsed_name_value_pair(self, method_name: str, content: str) -> Tuple[str, Any]:
        return (
            self._get_parsed_value_name(method_name),
            self._execute_parse_method(method_name, content)
        )

    def _get_parsed_value_name(self, method_name: str) -> str:
        return method_name.replace(
            self._KEYWORLD_PARSE, self._PLACEHOLDER_EMPTY, self._FIRST_ENTRY
        )

    def _execute_parse_method(self, method_name: str, content: str) -> Any:
        return getattr(self, method_name)(content)
