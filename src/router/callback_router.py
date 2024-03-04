"""File of callbacks for the bot"""

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from src.service.parser_json.ParseJson import ParseJson
from src.service.buttons.ButtonsService import ButtonService

callback_router = Router()


@callback_router.callback_query(F.data == "contacts")
async def answer_contact(message_user: CallbackQuery) -> Message:
    """Function to answer of CallbackQuery contacts

    Args:
        message_user (CallbackQuery): This obj. represents an incoming callback query from a callback button in an inline
        <https://core.telegram.org/bots/features#inline-keyboards>

    Returns:
        Message: This object represents a message.

    External Docs:
        https://core.telegram.org/bots/api#callbackquery
        https://core.telegram.org/bots/api#message
    """
    if isinstance(message_user.message, Message):
        buttons_data = ParseJson("src/json_files/contacts.json").create_dict()
        if isinstance(buttons_data, dict):
            buttons = ButtonService(buttons_data).create_buttons()
            buttons.adjust(2)
            msg = await message_user.message.answer(
                "Это контакты", reply_markup=buttons.as_markup()
            )
    return msg


@callback_router.callback_query(F.data == "configurator")
async def answer_configurator(message_user: CallbackQuery) -> Message:
    if isinstance(message_user.message, Message):
        msg = await message_user.message.answer("Это конфигуратор")
    return msg


@callback_router.callback_query(F.data == "catalog")
async def answer_catalog(message_user: CallbackQuery) -> Message:
    if isinstance(message_user.message, Message):
        msg = await message_user.message.answer("Это товары")
    return msg
