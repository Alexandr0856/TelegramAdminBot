from os import environ
from dotenv import load_dotenv

load_dotenv(f".{environ.get('ENV', 'development')}.env")


class TgKey:
    TOKEN: str = environ.get("TOKEN")
    CHANNEL_ID: int = int(environ.get("CHANNEL_ID"))
    MIN_DELAY: int = int(environ.get("MIN_DELAY", 10))
    MAX_DELAY: int = int(environ.get("MAX_DELAY", 60))


class PostgresEnv:
    USER: str = environ.get("POSTGRES_USER")
    HOST: str = environ.get("POSTGRES_HOST")
    PORT: int = int(environ.get("POSTGRES_PORT"))
    PASSWORD: str = environ.get("POSTGRES_PASSWORD")
    DB_NAME: str = environ.get("POSTGRES_DB")
