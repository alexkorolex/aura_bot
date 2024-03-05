"""User Repository for working with base"""

import logging
from aiogram import types
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, NoResultFound
from src.models.users import UsersModelORM
from src.schemas.user_telegram import UserTelegramSchema
from src.database.database import Database


class UserRepositoryAlchemy:
    """User repository"""

    _database: Database = Database()

    @classmethod
    def __convert_schema(cls, message: types.Message) -> UserTelegramSchema:
        if isinstance(message.from_user, types.User):
            userid = message.from_user.id
            username = message.from_user.username
            url = message.from_user.url
        return UserTelegramSchema(
            telegram_id=str(userid),
            username=username,
            link=url,
        )

    @classmethod
    async def __find_element(cls, session: AsyncSession, user: UsersModelORM) -> bool:
        """Function to find the user

        Args:
            session (AsyncSession): AsyncSession
            user (UsersModelORM): UsersModelORM

        Returns:
            bool: True if user exists. False otherwise
        """
        try:
            query = (
                select(UsersModelORM)
                .where(UsersModelORM.telegram_id == user.telegram_id)
                .where(UsersModelORM.link == user.link)
            )
            result = await session.execute(query)
            result = result.scalar_one_or_none()  # type: ignore
            if result:
                return True
            else:
                return False
        except NoResultFound:
            return False

    @classmethod
    async def __close(cls, session: AsyncSession) -> True:
        await session.close()  # type: ignore

    @classmethod
    async def add(cls, message: types.Message) -> None:
        """Add user"""
        user = cls.__convert_schema(message)
        if cls._database is not None:
            async with cls._database.session() as session:  # type: ignore
                userorm = UsersModelORM(
                    telegram_id=user.telegram_id,
                    username=user.username,
                    link=user.link,
                )
                try:
                    result_search = await cls.__find_element(
                        session=session, user=userorm
                    )
                    if result_search is not True:
                        session.add(userorm)
                        await session.commit()
                except IntegrityError:
                    logging.info("User already exists")
                except Exception as e:
                    logging.error("Error occurred while adding user to database: %s", e)
                finally:
                    await cls.__close(session)
