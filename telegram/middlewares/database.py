from typing import Dict, Any, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message
from psycopg2 import pool as pg_pool

from misc.env import PostgresEnv
from misc.pg_utils import Postgres
from misc.logger_conf import logger


class DatabaseMiddleware(BaseMiddleware):
    """
    This middleware is used to connect to the database.
    """

    def __init__(self):
        super().__init__()
        self.conn_pool = pg_pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            database=PostgresEnv.DB_NAME,
            user=PostgresEnv.USER,
            password=PostgresEnv.PASSWORD,
            host=PostgresEnv.HOST,
            port=PostgresEnv.PORT
        )

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ):
        connection = self.conn_pool.getconn()
        data['pg'] = Postgres(connection)
        logger.info(f"Connected to the database")

        try:
            logger.info(f"Pinged the database: {data['pg'].ping()}")
            await handler(event, data)
        finally:
            self.conn_pool.putconn(connection)
