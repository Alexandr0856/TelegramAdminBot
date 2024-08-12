import json

from aiogram import Bot
from aiogram.types import FSInputFile

from misc.env import TgKey
from misc import logger


async def get_file_id(bot: Bot, name: str):
    with open("assets/assets_ids.json", "r") as json_file:
        assets = json.load(json_file)

    if file_id := assets.get(name):
        return file_id

    logger.info(f"Uploading {name} to Telegram")

    message = await bot.send_photo(
        chat_id=TgKey.MEDIA_CHAT_ID,
        photo=FSInputFile(f"assets/{name}"),
        caption=name
    )

    file_id = message.photo[-1].file_id

    assets[name] = file_id
    with open("assets/assets_ids.json", "w") as json_file:
        json.dump(assets, json_file)

    return file_id

