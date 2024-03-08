"""User Repository for working with base"""

import logging
from typing import Sequence, Tuple
from sqlalchemy import select, Row
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, NoResultFound
from src.models.category import CategoryModelORM
from src.database.database import Database


class CategoryRepositoryAlchemy:
    """User repository"""

    _database: Database = Database()

    @classmethod
    async def __close(cls, session: AsyncSession) -> True:
        await session.close()  # type: ignore

    @classmethod
    async def add(cls, category: CategoryModelORM) -> None:
        """Add user"""
        if cls._database is not None:
            async with cls._database.session() as session:  # type: ignore
                try:
                    session.add(category)
                    await session.commit()
                except IntegrityError:
                    logging.info("User already exists")
                except Exception as e:
                    logging.error("Error occurred while adding user to database: %s", e)
                finally:
                    await cls.__close(session)

    @classmethod
    async def find_element(cls) -> None | Sequence[Row[Tuple[CategoryModelORM]]]:
        """Function to find the user

        Args:
            session (AsyncSession): AsyncSession
            user (UsersModelORM): UsersModelORM

        Returns:
            bool: True if user exists. False otherwise
        """
        async with cls._database.session() as session:  # type: ignore
            try:
                query = select(CategoryModelORM)
                result = await session.execute(query)
                result = result.all()  # type: ignore
                if result:
                    return result
            except NoResultFound as e:
                logging.error("Fail to search: %s", e)

            return None


async def insert_category_data() -> None:
    """Insert fake data"""
    categories = [
        "Parfume",
        "Diffuser",
        "Samples",
    ]
    for category in categories:
        await CategoryRepositoryAlchemy().add(CategoryModelORM(id=None, name=category))
