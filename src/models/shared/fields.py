"""Custom fields for models"""

import datetime
from typing import Annotated
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import mapped_column, MappedColumn


def foreign_key(
    column: str, cascade: str | None = "CASCADE", primary_key: bool = False
) -> MappedColumn:
    return mapped_column(ForeignKey(column, ondelete=cascade), primary_key=primary_key)


integer_primary_key = Annotated[int, mapped_column(primary_key=True)]
date_create = Annotated[
    datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))
]
