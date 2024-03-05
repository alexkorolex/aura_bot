from typing import Optional
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from src.service.manager.BotManagerFacade import BotManagerFacade


message_router = Router()


@message_router.message(Command("start"))
async def start(message_user: Message) -> Optional[Message]:
    bot_service = BotManagerFacade(
        path_file_json="src/json_files/main.json", message=message_user
    )
    result = await bot_service.send_message(
        text="Привет! С вами парфюмерный магазин Aura!"
    )
    return result
