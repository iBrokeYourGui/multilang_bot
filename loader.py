# Глобальные переменные объекты

# import logging
from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

# logging.basicConfig(level=logging.INFO)
# bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
