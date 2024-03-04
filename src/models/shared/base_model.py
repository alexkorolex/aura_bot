"""Base class for ORM and DTO"""
from typing import Annotated
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String

str_32 = Annotated[str, 32]
str_64 = Annotated[str, 64]
str_512 = Annotated[str, 512]
str_1024 = Annotated[str, 1024]
str_2048 = Annotated[str, 2048]


class BaseModelORM(DeclarativeBase):
    """Base class for ORM and DTO"""

    type_annotation = {
        str_32: String(32),
        str_64: String(64),
        str_512: String(512),
        str_1024: String(1024),
        str_2048: String(2048),
    }

    def __repr__(self) -> str:
        cols = []
        for col in self.__table__.columns.keys():
            cols.append(f"{col}={getattr(self, col)}")
        return f"<{self.__class__.__name__} {','.join(cols)}>"
