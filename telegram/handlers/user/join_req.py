import random
import asyncio

from aiogram import Bot
from aiogram.types import ChatJoinRequest

from misc.env import TgKey
from misc import logger, Pg
from misc.assets import IMAGE_DIYAR
from keyboards import get_welcome_keyboard
from locales import get_message_text


async def approve_request(chat_join: ChatJoinRequest, bot: Bot, pg: Pg):
    try:
        user_id = chat_join.from_user.id
        username = chat_join.from_user.username

        logger.info(f"User {username}[{user_id}] joined the chat")

        pg.add_chat(chat_join.chat.id, chat_join.chat.title)
        pg.add_user_with_chat(user_id, chat_join.chat.id, username, chat_join.from_user.first_name, chat_join.from_user.last_name)
        pg.commit()

        delay = random.randint(TgKey.MIN_DELAY, TgKey.MAX_DELAY)
        await asyncio.sleep(delay)

        await chat_join.approve()
        await bot.send_photo(
            chat_id=chat_join.from_user.id,
            photo=IMAGE_DIYAR,
            caption=get_message_text("welcome", "ru"),
            parse_mode="MarkdownV2",
            reply_markup=get_welcome_keyboard()
        )
        logger.info(f"User {username}[{user_id}] approved after {delay} seconds")
    except Exception as e:
        logger.error(f"Error in approve_request: {e}")
