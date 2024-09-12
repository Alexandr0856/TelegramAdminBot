from aiogram.utils.keyboard import InlineKeyboardBuilder

from locales import get_button_text


def get_welcome_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=get_button_text("main_text", "ru"),
        url=get_button_text("main_url", "ru")
    )
    return builder.as_markup()
