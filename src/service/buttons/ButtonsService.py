from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder
from aiogram.types import InlineKeyboardButton


class ButtonService:
    """Class of working with a buttons of bot

    Returns:
        _type_: InlineKeyboardButton if the button is correct
    """

    _buttons = None

    def __init__(self, buttons: dict):
        self._buttons = InlineKeyboardBuilder()
        for button in buttons:
            massive = buttons[button]
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

    def create_buttons(self) -> InlineKeyboardBuilder:
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
