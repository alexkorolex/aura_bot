"File Database"
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.setting.settings import settings
from src.models.shared.base_model import BaseModelORM
from src.models.users import UsersModelORM  # noqa # pylint: disable=unused-import


class Database:
    """Class to create a connection and work with database MySQL

    Returns:
        AsyncEngine: AsyncEngine object of mysql

    External Docs:
        https://pydocbrowser.github.io/sqlalchemy/latest/sqlalchemy.dialects.mysql.asyncmy.html
    """

    _instance = None
    engine = None
    session = None

    def __new__(cls) -> "Database":

        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.engine = create_async_engine(
                url=settings._DATABASE_URL_ASYNC,
                echo=True,
            )
            cls._instance.session = async_sessionmaker(
                bind=cls._instance.engine,
            )
            cls.session = cls._instance.session
        return cls._instance

    @staticmethod
    def get_new_async_sessionmaker() -> async_sessionmaker:
        """Get new async session"""
        async_engine = create_async_engine(
            url=settings._DATABASE_URL_ASYNC,
            echo=False,
            pool_size=5,
            max_overflow=10,
        )
        return async_sessionmaker(bind=async_engine)

    def __init__(self) -> None:
        """Initialize the database"""
        if self.session is not None:
            self.session = self.session

    def create_async_session(self) -> AsyncSession:
        """Create async session"""
        new_async_session = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
        )
        return new_async_session()

    async def create_tables(self) -> None:
        """Asynchronously initialize the database"""
        async with self.engine.begin() as connection:  # type: ignore
            print("Starting database initialization...")
            await connection.run_sync(BaseModelORM.metadata.create_all)
            print("Database tables created.")

    async def drop_tables(self) -> None:
        """Asynchronously drop all tables with CASCADE"""
        async with self.engine.begin() as connection:  # type: ignore
            print("Starting database initialization...")
            await connection.run_sync(BaseModelORM.metadata.drop_all)
            print("Database tables created.")
