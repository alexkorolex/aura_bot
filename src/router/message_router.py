from typing import Optional
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from src.service.buttons.ButtonsService import ButtonService
from src.service.parser_json.ParseJson import ParseJson


message_router = Router()


@message_router.message(Command("start"))
async def start(message_user: Message) -> Optional[Message]:
    data_buttons = ParseJson("src/json_files/main.json").create_dict()
    if isinstance(data_buttons, dict):
        buttons = ButtonService(buttons=data_buttons).create_buttons()
        buttons.adjust(2)
        message = await message_user.answer("Привет!", reply_markup=buttons.as_markup())
        return message
    return None
