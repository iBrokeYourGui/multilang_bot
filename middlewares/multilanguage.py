from typing import Tuple, Any
from config import LANG_STORAGE
from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware


class MultiLang(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        user: types.User = types.User.get_current()
        if LANG_STORAGE.get(user.id) is None:
            LANG_STORAGE[user.id] = "ru"
        *_, data = args
        language = data['locale'] = LANG_STORAGE[user.id]
        return language
