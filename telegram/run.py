import asyncio
import contextlib

from aiogram import Bot
from aiohttp import ClientSession, ClientTimeout
from misc.env import TelegramEnv
from dispatcher import get_dispatcher


async def start_bot():
    dp = get_dispatcher()

    session = ClientSession(timeout=ClientTimeout(total=60))
    bot = Bot(token=TelegramEnv.TOKEN, session=session)

    await dp.start_polling(bot)


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start_bot())
