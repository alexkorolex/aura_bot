from aiogram.types import CallbackQuery


class QueryWorker:

    def __init__(self, query: CallbackQuery) -> None:
        if query.data is not None:
            data = query.data.split("_")
            if len(data) == 1:
                self.query = query.data
            elif len(data) == 2:
                self.query = data[1]

    def find_element(self) -> int:
        if self.query == "Parfume":
            result = 1
        elif self.query == "Diffuser":
            result = 2
        elif self.query == "Samples":
            result = 3
        return result
