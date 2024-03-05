from aiogram import Bot, Dispatcher
from src.setting.settings import settings
from src.router.message_router import message_router
from src.router.callback_router import callback_router

from src.database.database import Database


async def main() -> None:
    """Function to run the bot"""
    if settings._TOKEN is not None:
        database = Database()
        await database.drop_tables()
        await database.create_tables()
        bot = Bot(settings._TOKEN)
        dp = Dispatcher()
        dp.include_routers(message_router, callback_router)
        await dp.start_polling(bot)
