from aiogram import Bot, Dispatcher
from src.setting.settings import settings
from src.repositories.CategoryRepository import insert_category_data
from src.repositories.ProductRepository import (
    insert_product_data,
)
from src.router.message_router import message_router
from src.router.callback_router import callback_router
from src.database.database import Database


async def main() -> None:
    """Function to run the bot"""
    if settings._TOKEN is not None:
        database = Database()
        await database.drop_tables()
        await database.create_tables()
        await insert_category_data()
        await insert_product_data()
        bot = Bot(settings._TOKEN)
        dp = Dispatcher()
        dp.include_routers(message_router, callback_router)
        await dp.start_polling(bot)
