from aiogram import Bot
from aiogram.types import Message

from misc import Pg
from misc import logger
from misc.assets import IMAGE_DIYAR
from keyboards import get_welcome_keyboard
from locales import get_message_text


async def help_handler(message: Message, bot: Bot) -> None:
    try:
        user_id = message.from_user.id
        username = message.from_user.username or f"{message.from_user.first_name} {message.from_user.last_name}"

        logger.info(f"User {username}[{user_id}] requested help")
        await message.answer(get_message_text("help", "ru"))
        logger.info(f"User {username}[{user_id}] success received help")
    except Exception as e:
        logger.error(f"Error in help_handler: {e}")


async def start_handler(message: Message, bot: Bot, pg: Pg) -> None:
    try:
        user_id = message.from_user.id
        username = message.from_user.username or f"{message.from_user.first_name} {message.from_user.last_name}"

        logger.info(f"User {username}[{user_id}] started the bot")

        # await message.answer(get_message_text("welcome", "ru"), parse_mode="MarkdownV2")
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=IMAGE_DIYAR,
            caption=get_message_text("welcome", "ru"),
            parse_mode="MarkdownV2",
            reply_markup=get_welcome_keyboard()
        )
        logger.info(f"User {username}[{user_id}] success received welcome message")
    except Exception as e:
        logger.error(f"Error in start_handler: {e}")
