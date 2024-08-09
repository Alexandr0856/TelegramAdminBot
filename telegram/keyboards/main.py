from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_welcome_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="НАПИСАТЬ", url="https://t.me/DiyarArbitrage")
    return builder.as_markup()
