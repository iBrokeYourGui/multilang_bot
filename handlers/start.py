import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text, Message
# from utils.set_bot_commands import set_default_commands

from loader import dp
from middlewares import _
from keyboards import main_keyboard


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # await set_default_commands(dp, message.chat.id)
    await message.answer(_("Привет"), reply_markup=main_keyboard)
