from aiogram import Bot

from misc.env import TgKey
from misc.assets import IMAGE_DIYAR


async def check_file(file_id: str):
    async with Bot(token=TgKey.TOKEN) as bot:
        try:
            file_info = await bot.get_file(file_id)
            print(f"File is available. File path: {file_info.file_path}")
        except Exception as e:
            print(f"File is not available or there was an error: {e}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(check_file(IMAGE_DIYAR))
