import random
import asyncio

from aiogram import Bot
from aiogram.types import ChatJoinRequest

from misc.env import TgKey
from misc import logger, Pg
from misc.assets import get_file_id
from keyboards import get_welcome_keyboard
from locales import get_message_text


async def approve_request(chat_join: ChatJoinRequest, bot: Bot, pg: Pg):
    chat_id = chat_join.chat.id
    user_id = chat_join.from_user.id
    username = chat_join.from_user.username

    logger.info(f"User {username}[{user_id}] joined the chat")

    pg.add_chat(chat_id, chat_join.chat.title)
    pg.add_user_with_chat(
        user_id, chat_id, username,
        chat_join.from_user.first_name, chat_join.from_user.last_name
    )

    pg.commit()

    delay = random.randint(TgKey.MIN_DELAY, TgKey.MAX_DELAY)
    await asyncio.sleep(delay)

    for attempt in range(retries := TgKey.RETRIES):
        try:
            member = await bot.get_chat_member(chat_id, user_id)

            if member.status != "left":
                logger.info(f"User {username}[{user_id}] already in chat")
                break

            result = await chat_join.approve()

            if not result:
                logger.error(f"User {username}[{user_id}] not approved in {attempt} attempt")
                continue

            file_id = await get_file_id(bot, "diyar.png")

            await bot.send_photo(
                chat_id=chat_join.from_user.id,
                photo=file_id,
                caption=get_message_text("welcome", "ru"),
                parse_mode="MarkdownV2",
                reply_markup=get_welcome_keyboard()
            )
            logger.info(f"User {username}[{user_id}] approved after {delay} seconds")
            break
        except Exception as e:
            if "USER_ALREADY_PARTICIPANT" in str(e):
                logger.info(f"User {username}[{user_id}] already in chat")
                break

            if attempt == retries - 1:
                logger.error(f"Error in {attempt} attempt approve_request: {e}")
                await asyncio.sleep(TgKey.RETRIES_DELAY)
            else:
                logger.error(f"Error finale can't approve user {username}[{user_id}]: {e}")
                raise e
