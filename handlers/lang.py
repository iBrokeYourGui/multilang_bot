from aiogram import types
from aiogram.dispatcher.filters import IDFilter
from aiogram.utils.callback_data import CallbackData
from middlewares import _

from config import ADMINS, LANG_STORAGE
from keyboards import kbd_lang
from loader import dp

call_b = CallbackData("lang", "language")


@dp.message_handler(IDFilter(ADMINS), commands=["lang"])
async def text_three(message: types.Message):
    await message.answer(_("Установить язык"), reply_markup=kbd_lang)


@dp.callback_query_handler(call_b.filter())
async def change_langeage(call: types.CallbackQuery, callback_data: dict):
    lang = callback_data.get("language")
    LANG_STORAGE[call.from_user.id] = lang
    await call.message.answer(_("Язык установлен: ", locale=lang))
