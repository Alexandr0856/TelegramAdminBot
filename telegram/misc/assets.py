import os
import json

from aiogram import Bot
from aiogram.types import FSInputFile

from misc import logger
from misc.env import TelegramEnv, AssetsEnv


async def get_file_id(bot: Bot, name: str):
    assets_ids_path = os.path.join(AssetsEnv.ASSETS_DIR, "assets_ids.json")

    with open(assets_ids_path, "r") as json_file:
        assets = json.load(json_file)

    if file_id := assets.get(name):
        return file_id

    logger.info(f"Uploading {name} to Telegram")

    message = await bot.send_photo(
        chat_id=TelegramEnv.MEDIA_CHAT_ID,
        photo=FSInputFile(os.path.join(AssetsEnv.ASSETS_DIR, name)),
        caption=name
    )

    file_id = message.photo[-1].file_id

    assets[name] = file_id
    with open(assets_ids_path, "w") as json_file:
        json.dump(assets, json_file)

    return file_id
