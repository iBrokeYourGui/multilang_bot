from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from middlewares import _

kbd_lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=_('Русский'), callback_data="lang:ru"),
            InlineKeyboardButton(text=_('Английский'), callback_data="lang:en"),
        ]
    ]
)
