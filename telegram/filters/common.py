from aiogram import F

from misc.env import TelegramEnv


request_to_join = F.chat.id == TelegramEnv.CHANNEL_ID
