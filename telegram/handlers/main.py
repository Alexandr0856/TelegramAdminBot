from aiogram import Dispatcher

from .user import get_user_router
from .admin import get_admin_router


def register_all_handlers(dp: Dispatcher) -> None:
    routers = (
        get_user_router(),
        get_admin_router(),
    )

    for router in routers:
        dp.include_router(router)
