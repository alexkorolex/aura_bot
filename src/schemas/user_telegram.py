from typing import Optional
from pydantic import BaseModel


class UserTelegramSchema(BaseModel):
    """Class of UserTelegramSchema

    Args:
        BaseModel (_type_):Usage docs: https://docs.pydantic.dev/2.5/concepts/models/
            A base class for creating Pydantic models.
    """

    telegram_id: str
    username: Optional[str] = None
    link: str
