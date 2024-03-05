"""File BotManager"""

from typing import Optional
from aiogram.types import Message, CallbackQuery
from src.service.parser_json.ParseJson import ParseJson
from src.service.buttons.ButtonsService import ButtonService
from src.service.bot.BotBase import BotBase


class BotManagerFacade:
    """Class to generate messages for bot"""

    def __init__(
        self, message: Message | CallbackQuery, path_file_json: str = "None"
    ) -> None:
        if path_file_json != "None":
            self.parse_json = ParseJson(path_file_json)
            self.buttons = ButtonService
        self.bot = BotBase(message)

    async def send_message(self, text: str) -> Optional[Message]:
        """Function to send a message
         Args:
            text (str): Text to send by bot
        Returns:
            Optional[Message]: This object represents a message.

        External Docs:
            https://core.telegram.org/bots/api#message

        """
        data_buttons = self.parse_json.create_dict()
        if isinstance(data_buttons, dict):
            buttons = self.buttons(buttons=data_buttons).create_buttons()
            buttons.adjust(2)
            message = await self.bot.send_message(text=text, buttons=buttons)
            return message
        return None

    async def delete_and_send_message(self, text: str) -> Optional[Message]:
        """Function to send a message and delete old message
        Args:
            text (str): Text to send by bot

        Returns:
            Optional[Message]: This object represents a message.

        External Docs:
            https://core.telegram.org/bots/api#message
        """
        await self.bot.delete_message()
        message = await self.send_message(text)
        if isinstance(message, Message):
            return message
        return None