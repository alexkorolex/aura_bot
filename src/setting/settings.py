"""File of Settings"""

import os


class Settings:
    """Settings class"""

    _TOKEN = os.getenv("TOKEN")
    _MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
    _MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
    _MYSQL_USER = os.getenv("MYSQL_USER")
    _MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    _HOST = os.getenv("HOST")
    _PORT = os.getenv("PORT")
    _DATABASE_URL_ASYNC = f"mysql+asyncmy://{_MYSQL_USER}:{_MYSQL_PASSWORD}@{_HOST}:{_PORT}/{_MYSQL_DATABASE}"


settings = Settings()
