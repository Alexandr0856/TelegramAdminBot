from os import environ
from dotenv import load_dotenv

load_dotenv(f".{environ.get('ENV', 'development')}.env")


class TelegramEnv:
    TOKEN: str = environ.get("TOKEN")

    CHANNEL_ID: int = int(environ.get("CHANNEL_ID"))
    MEDIA_CHAT_ID: int = int(environ.get("MEDIA_CHAT_ID"))

    MIN_DELAY: int = int(environ.get("MIN_DELAY", 10))
    MAX_DELAY: int = int(environ.get("MAX_DELAY", 60))

    RETRIES: int = int(environ.get("RETRIES", 3))
    RETRIES_DELAY: int = int(environ.get("RETRIES_DELAY", 5))


class PostgresEnv:
    USER: str = environ.get("POSTGRES_USER")
    HOST: str = environ.get("POSTGRES_HOST")
    PORT: int = int(environ.get("POSTGRES_PORT"))
    PASSWORD: str = environ.get("POSTGRES_PASSWORD")
    DB_NAME: str = environ.get("POSTGRES_DB")


class AssetsEnv:
    ASSETS_DIR: str = environ.get("ASSETS_DIR", "assets")
    WELCOME_PHOTO: str = environ.get("WELCOME_PHOTO", "welcome.png")
