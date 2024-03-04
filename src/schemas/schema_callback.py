from enum import Enum
from aiogram.filters.callback_data import CallbackData


class Action(str, Enum):
    ban = "ban"
    kick = "kick"
    warn = "warn"


class AdminAction(CallbackData, prefix="adm"):
    action: Action
    chat_id: int
    user_id: int
