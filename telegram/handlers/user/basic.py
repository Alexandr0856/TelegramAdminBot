from aiogram import Bot
from aiogram.types import Message

from misc import logger
from misc.env import AssetsEnv
from misc.assets import get_file_id
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


async def start_handler(message: Message, bot: Bot) -> None:
    try:
        user_id = message.from_user.id
        username = message.from_user.username or f"{message.from_user.first_name} {message.from_user.last_name}"

        logger.info(f"User {username}[{user_id}] started the bot")

        file_id = await get_file_id(bot, AssetsEnv.WELCOME_PHOTO)
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=file_id,
            caption=get_message_text("welcome", "ru"),
            parse_mode="MarkdownV2",
            reply_markup=get_welcome_keyboard()
        )
        logger.info(f"User {username}[{user_id}] success received welcome message")
    except Exception as e:
        logger.error(f"Error in start_handler: {e}")
