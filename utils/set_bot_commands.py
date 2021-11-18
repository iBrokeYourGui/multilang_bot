import logging
from aiogram import types


async def set_default_commands(dp):
    data = [
        # Commands in private chats (English and Russian)
        (
            [
                types.BotCommand(command="start", description="Bot start"),
                types.BotCommand(command="help", description="Show help"),
                types.BotCommand(command="lang", description="NEW hoose language")
            ],
            types.BotCommandScopeAllPrivateChats(),
            "en"
        ),
        (
            [
                types.BotCommand(command="start", description="Запуск бота"),
                types.BotCommand(command="help", description="Вывести справку"),
                types.BotCommand(command="lang", description="NEW Выбрать язык")
            ],
            types.BotCommandScopeAllPrivateChats(),
            "ru"
        ),
    ]
    for commands_list, commands_scope, language in data:
        await dp.bot.set_my_commands(commands=commands_list, scope=commands_scope, language_code=language)
    logging.info("Базовые команды успешно установлены")
