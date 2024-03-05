"""File BotBase class"""

from typing import Optional
from aiogram.types import Message, CallbackQuery
from aiogram.methods import DeleteMessage
from aiogram.utils.keyboard import InlineKeyboardBuilder


class BotBase:
    """Class of generate messages for bot."""

    def __init__(self, message: Message | CallbackQuery):
        if isinstance(message, Message):
            self.message = message
        if isinstance(message, CallbackQuery):
            message = message.message  # type: ignore
            if isinstance(message, Message):
                self.message = message
        if message is not None:
            bot = message.bot
            if bot is not None:
                self.bot = bot

    async def delete_message(self) -> bool:
        """Function to delete a message

        Returns:
            bool: If message was deleted successfully - True. False otherwise.
        """
        await self.bot(
            DeleteMessage(
                chat_id=self.message.chat.id, message_id=self.message.message_id
            )
        )
        return True

    async def send_message(
        self, text: str, buttons: InlineKeyboardBuilder
    ) -> Optional[Message]:
        """Function to start a message

        Args:
            text (str): Text of bot message
            buttons (InlineKeyboardBuilder): Buttons of bot message

        Returns:
            Optional[Message]: This object represents a message.

        Source:
            https://core.telegram.org/bots/api#message
        """
        message = await self.message.answer(text, reply_markup=buttons.as_markup())
        return message
