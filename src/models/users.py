"""User model ORM"""

import sqlalchemy as sa
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.models.shared.fields import integer_primary_key
from src.models.shared.base_model import BaseModelORM, str_32, str_64


class UsersModelORM(BaseModelORM):
    """User schema ORM"""

    __tablename__ = "users_telegram"
    id: Mapped[integer_primary_key]
    telegram_id: Mapped[int] = mapped_column(sa.BigInteger, sa.Identity())
    username: Mapped[str_32] = mapped_column(String(32), nullable=True)
    link: Mapped[str_64] = mapped_column(String(64))
