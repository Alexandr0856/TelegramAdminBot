from aiogram import Router

from .join_req import approve_request
from .command import start_handler, help_handler

from filters.common import request_to_join_filter
from filters.commands import start_command, help_command


def get_user_router() -> Router:
    userRouter = Router()

    userRouter.message.register(start_handler, start_command)
    userRouter.message.register(help_handler, help_command)

    userRouter.chat_join_request.register(approve_request, request_to_join_filter)

    return userRouter
