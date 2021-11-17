from aiogram import executor

from loader import dp, bot
# порядок импорта надо строго соблюдать
import middlewares, handlers
# from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    # Устанавливаем дефолтные команды
    await set_default_commands(dp)
    # # Уведомляет о запуске
    # await on_startup_notify(dp)


async def on_shutdown(dp):
    session = await bot.get_session()
    await session.close()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)

