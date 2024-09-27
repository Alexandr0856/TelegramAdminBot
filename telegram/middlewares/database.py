from typing import Dict, Any, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message
from psycopg2 import pool as pg_pool, OperationalError

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
        max_retries = 3

        for attempt in range(max_retries):
            connection = None

            try:
                connection = self.conn_pool.getconn()
                data['pg'] = Postgres(connection)
                logger.info(f"Connected to the database")
                logger.info(f"Pinged the database: {data['pg'].ping()}")

                await handler(event, data)
                break

            except OperationalError as e:
                logger.error(f"OperationalError on attempt {attempt + 1}: {e}")
                if attempt < max_retries - 1:
                    logger.info("Retrying...")
                else:
                    logger.error("Max retries reached. Unable to connect to the database.")

            except Exception as e:
                logger.error(f"An unexpected error occurred: {e}")
                break

            finally:
                if connection:
                    self.conn_pool.putconn(connection)
                else:
                    logger.warning("No connection was retrieved from the pool.")
