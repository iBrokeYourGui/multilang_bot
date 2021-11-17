from middlewares import _

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(_("Инлайн клавиатура"))],
        [
            KeyboardButton(_("Скрыть клавиатуру")),
            KeyboardButton(_("Удалить клавиатуру")),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)