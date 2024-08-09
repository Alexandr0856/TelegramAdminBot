from aiogram import F

from misc.env import TgKey


request_to_join = F.chat.id == TgKey.CHANNEL_ID
