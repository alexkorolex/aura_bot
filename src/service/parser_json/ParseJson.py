"""File of parse json files"""

import json


class ParseJson:

    _json = None

    def __init__(self, path_json: str):
        with open(path_json, "r", encoding="utf-8") as file:
            data = json.load(file)
        self._json = data

    def create_dict(self) -> dict | None:
        """Function to create a dictionary

        Returns:
            dict | None: Returns dictionary if it exists. None otherwise
        """
        if self._json is not None:
            return self._json
        return None
