"""File of callbacks for the bot"""

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from src.service.manager.BotManagerFacade import BotManagerFacade
from src.repositories.CategoryRepository import CategoryRepositoryAlchemy
from src.repositories.ProductRepository import ProductRepositoryAlchemy, file_set

callback_router = Router()


@callback_router.callback_query(F.data == "contacts")
async def answer_contact(message_user: CallbackQuery) -> Message | None:
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
    manager = BotManagerFacade(
        message=message_user, path_file_json="src/json_files/contacts.json"
    )
    message = await manager.delete_and_send_message("Это контакты")
    return message


@callback_router.callback_query(F.data == "configurator")
async def answer_configurator(message_user: CallbackQuery) -> Message:
    """Function to answer of CallbackQuery configuration

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
        msg = await message_user.message.answer("Это конфигуратор")
    return msg


@callback_router.callback_query(F.data == "catalog")
async def answer_catalog(message_user: CallbackQuery) -> Message | None:
    """Function to answer of CallbackQuery catalog

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
        result = await CategoryRepositoryAlchemy().find_element()
        if result is not None:
            message = await BotManagerFacade(
                message=message_user, data_sql=result, data_callback="main"
            ).delete_and_send_message("Это каталог товаров")
            return message
    return None


@callback_router.callback_query(F.data == "Parfume")
async def answer_parfume(message_user: CallbackQuery) -> Message | None:
    result = await ProductRepositoryAlchemy.find_element(1)
    if result is not None:
        message = await BotManagerFacade(
            message=message_user, data_sql=result, data_callback="catalog"
        ).delete_and_send_message("Это каталог товаров")
        return message
    return None


@callback_router.callback_query(F.data.in_(file_set))
async def answer_product(message_user: CallbackQuery) -> Message | None:
    print(message_user)
    return None


@callback_router.callback_query(F.data == "main")
async def open_start(message_user: CallbackQuery) -> Message | None:
    """Function to answer of CallbackQuery catalog

    Args:
        message_user (CallbackQuery): This obj. represents an incoming callback query from a callback button in an inline
        <https://core.telegram.org/bots/features#inline-keyboards>

    Returns:
        Message: This object represents a message.

    External Docs:
        https://core.telegram.org/bots/api#callbackquery
        https://core.telegram.org/bots/api#message
    """
    manager = BotManagerFacade(
        message=message_user, path_file_json="src/json_files/main.json"
    )
    message = await manager.delete_and_send_message("Главное меню")
    return message
