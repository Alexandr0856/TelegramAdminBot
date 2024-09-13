import asyncio
import contextlib

from aiogram import Bot
from misc.env import TelegramEnv
from dispatcher import get_dispatcher


async def start_bot():
    dp = get_dispatcher()

    bot = Bot(token=TelegramEnv.TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start_bot())
