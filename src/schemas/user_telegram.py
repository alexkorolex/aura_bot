from typing import Optional
from pydantic import BaseModel, HttpUrl


class UserTelegramSchema(BaseModel):
    """Class of UserTelegramSchema

    Args:
        BaseModel (_type_):Usage docs: https://docs.pydantic.dev/2.5/concepts/models/
            A base class for creating Pydantic models.
    """

    id: int
    username: Optional[str] = None
    link: HttpUrl
