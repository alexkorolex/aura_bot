"""User Repository for working with base"""

import logging
import json
from typing import Sequence, Tuple, Union
from sqlalchemy import select, Row
from sqlalchemy.orm import selectinload
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
    async def find_elements(
        cls,
        category_id: Union[int, None] = None,
        find_one_element: bool = False,
    ) -> None | Sequence[Row[Tuple[ProductModelORM]]] | ProductModelORM:
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
                    query = (
                        select(ProductModelORM)
                        .where(ProductModelORM.category_id == category_id)
                        .options(selectinload(ProductModelORM.category))
                    )
                else:
                    query = select(ProductModelORM)
                result = await session.execute(query)
                if find_one_element is False:
                    result = result.all()  # type: ignore
                else:
                    result = result.scalar_one_or_none()
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
            description="Black mama - унисекс аромат.\n\nЖенщина за 30 в черном платье пребывает вечером в дорогом ресторане Москвы. В воздухе царит запах табака и ванили. Начальные ноты - мягкий табак, который завлекает противоположный пол и интригует, а затем, после приятной беседы в ресторане, раскрывается пленительный запах ванили.",
            composition="70% 97% ethanol\n30% aromatic oils",
            application="Рекомендуем наносить на очищенное и распаренное тело для полного раскрытия парфюмерной композиции 1-2 пшика",
            sex="unisex",
            volume=50,
            flavor_group="Набор ароматов",
            top_notes="табак, специи",
            middle_notes="ваниль, цветок табака, какао, бобы тонка",
            basic_notes="дерево, фрукты",
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


def create_list_of_products(file_path_json: str) -> set:
    file_set = set()
    with open(file_path_json, "r", encoding="utf-8") as file:
        json_file = json.load(file)
        for json_data in json_file:
            file_set.add(json_file[json_data])
    return file_set


file_set_product = create_list_of_products("src/json_files/products.json")
file_set_category = create_list_of_products("src/json_files/category.json")
