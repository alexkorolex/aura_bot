"""User Repository for working with base"""

import logging
import json
from typing import Sequence, Tuple, Union
from sqlalchemy import select, Row
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, NoResultFound
from src.models.product import ProductModelORM
from src.database.database import Database


class ProductRepositoryAlchemy:
    """User repository"""

    _database: Database = Database()

    @classmethod
    async def __close(cls, session: AsyncSession) -> True:
        await session.close()  # type: ignore

    @classmethod
    async def add(cls, product: ProductModelORM) -> None:
        """Add user"""
        if cls._database is not None:
            async with cls._database.session() as session:  # type: ignore
                try:
                    session.add(product)
                    await session.commit()
                except IntegrityError:
                    logging.info("User already exists")
                except Exception as e:
                    logging.error("Error occurred while adding user to database: %s", e)
                finally:
                    await cls.__close(session)

    @classmethod
    async def find_element(
        cls,
        category_id: Union[int, None] = None,
    ) -> None | Sequence[Row[Tuple[ProductModelORM]]]:
        """Function to find the user

        Args:
            session (AsyncSession): AsyncSession
            user (UsersModelORM): UsersModelORM

        Returns:
            bool: True if user exists. False otherwise
        """
        async with cls._database.session() as session:  # type: ignore
            try:
                if category_id is not None:
                    query = select(ProductModelORM).where(
                        ProductModelORM.category_id == category_id
                    )
                else:
                    query = select(ProductModelORM)
                result = await session.execute(query)
                result = result.all()  # type: ignore
                if result:
                    return result
            except NoResultFound as e:
                logging.error("Fail to search: %s", e)

            return None


async def insert_product_data() -> None:
    """Insert fake data"""

    await ProductRepositoryAlchemy().add(
        ProductModelORM(
            id=None,
            name="Black Mama",
            price=6990,
            description="Описание BM",
            composition="Состав BM",
            application="Применение",
            sex="man",
            volume=50,
            flavor_group="Набор ароматов",
            top_notes="Верхние ноты",
            middle_notes="Средние ноты",
            basic_notes="Базовые ноты",
            category_id=1,
        )
    )
    await ProductRepositoryAlchemy().add(
        ProductModelORM(
            id=None,
            name="White Mama",
            price=6990,
            description="Описание BM",
            composition="Состав BM",
            application="Применение",
            sex="man",
            volume=50,
            flavor_group="Набор ароматов",
            top_notes="Верхние ноты",
            middle_notes="Средние ноты",
            basic_notes="Базовые ноты",
            category_id=2,
        )
    )


# async def create_list_of_product() -> set:
#     file = set()
#     result = await ProductRepositoryAlchemy().find_element()
#     if result is not None:
#         for data in result:
#             data_info = data._mapping._data[0]
#             file.add(data_info.name)
#     return file


def create_list_of_products() -> set:
    file_set = set()
    with open("src/json_files/products.json", "r", encoding="utf-8") as file:
        json_file = json.load(file)
        for json_data in json_file:
            file_set.add(json_file[json_data])
    return file_set


file_set = create_list_of_products()
