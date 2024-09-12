from aiogram import Bot

from misc.env import TelegramEnv


async def check_file(file_id: str):
    async with Bot(token=TelegramEnv.TOKEN) as bot:
        try:
            file_info = await bot.get_file(file_id)
            print(f"File is available. File path: {file_info.file_path}")
        except Exception as e:
            print(f"File is not available or there was an error: {e}")
