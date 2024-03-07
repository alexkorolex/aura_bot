"""Product model ORM"""

from enum import Enum
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.shared.fields import integer_primary_key
from src.models.category import CategoryModelORM
from src.models.shared.base_model import BaseModelORM, str_32, str_2048, str_64, str_512


class Sex(Enum):
    man = "man"
    woman = "woman"
    unisex = "unisex"


class ProductModelORM(BaseModelORM):
    """Product schema ORM"""

    __tablename__ = "products"

    id: Mapped[integer_primary_key]  # id of the product
    name: Mapped[str_32] = mapped_column(String(32))  # name of the product
    price: Mapped[int]  # price of the product
    description: Mapped[str_2048] = mapped_column(
        String(2048)
    )  # description of the product
    composition: Mapped[str_64] = mapped_column(
        String(64)
    )  # composition (состав) of the product
    application: Mapped[str_512] = mapped_column(
        String(512)
    )  # application (применение) of the product
    sex: Mapped[Sex]  # gender-specific
    volume: Mapped[int]  # volume of the product
    flavor_group: Mapped[str_32] = mapped_column(
        String(32), nullable=True
    )  # flavor group
    top_notes: Mapped[str_64] = mapped_column(
        String(64), nullable=True
    )  # top notes (Верхние ноты) of the product
    middle_notes: Mapped[str_64] = mapped_column(
        String(64), nullable=True
    )  # middle notes (Средние ноты) of the product
    basic_notes: Mapped[str_64] = mapped_column(
        String(64), nullable=True
    )  # basic notes (Базовые ноты) of the product

    producer: Mapped[str_32] = mapped_column(
        String(32), default="AURA"
    )  # producer (производитель) of the product

    category: Mapped[CategoryModelORM] = relationship(
        "CategoryModelORM", back_populates="products"
    )
    category_id = Column(Integer, ForeignKey("category.id"))
