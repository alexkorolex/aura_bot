from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder
from aiogram.types import InlineKeyboardButton
from src.models.product import ProductModelORM
from src.models.category import CategoryModelORM


class ButtonService:
    """Class of working with a buttons of bot

    Returns:
        _type_: InlineKeyboardButton if the button is correct
    """

    _buttons = None

    def __init__(self, buttons_dict: dict = None, buttons_tuple: tuple = None, data_callback: str = None, iter_data=False):  # type: ignore
        self._buttons = InlineKeyboardBuilder()
        if buttons_dict is not None:
            for button in buttons_dict:
                massive = buttons_dict[button]
                keys = list(massive.keys())
                if keys[1] == "url":
                    self._buttons.row(
                        InlineKeyboardButton(text=massive["text"], url=massive["url"])
                    )
                elif keys[1] == "callback_data":
                    self._buttons.row(
                        InlineKeyboardButton(
                            text=massive["text"], callback_data=massive["callback_data"]
                        )
                    )
        if buttons_tuple is not None and data_callback is not None:
            if iter_data is not False:
                for button in buttons_tuple:
                    data_button = button._mapping._data[0]
                    if isinstance(data_button, CategoryModelORM):
                        self._buttons.row(
                            InlineKeyboardButton(
                                text=data_button.name, callback_data=data_button.name  # type: ignore
                            )
                        )
                    if isinstance(data_button, ProductModelORM):
                        self._buttons.row(
                            InlineKeyboardButton(
                                text=data_button.name,
                                callback_data=f"{data_button.name}_{data_button.category.name}",
                            )
                        )

            self._buttons.row(
                InlineKeyboardButton(text="Назад", callback_data=data_callback)
            )

    def create_buttons(self) -> InlineKeyboardBuilder:
        """Function to create buttons for bot format InlineKeyboardBuilder

        Returns:
            InlineKeyboardBuilder: Inline keyboard builder inherits all methods from generic builder
        """
        if self._buttons is not None:
            buttons = self._buttons
        return buttons

    @classmethod
    def create_columns(
        cls, number_columns: int
    ) -> KeyboardBuilder[InlineKeyboardButton] | None:
        if cls._buttons is not None:
            buttons = cls._buttons.adjust(number_columns)
        if isinstance(buttons, KeyboardBuilder):
            return buttons

        return None
