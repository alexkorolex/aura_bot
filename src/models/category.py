"""Category model ORM"""

from enum import Enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.shared.fields import integer_primary_key
from src.models.shared.base_model import BaseModelORM, str_32


class CategoryProduct(Enum):
    parfume = "parfume"
    diffuser = "diffuser"
    samples = "samples"


class CategoryModelORM(BaseModelORM):
    """Category schema ORM"""

    __tablename__ = "category"

    id: Mapped[integer_primary_key]
    name: Mapped[CategoryProduct]
    category: Mapped[str_32] = mapped_column(String(32))

    products: Mapped[list["ProductModelORM"]] = relationship(back_populates="category")  # type: ignore
