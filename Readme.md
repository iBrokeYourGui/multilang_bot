### Реализация мультиязычности в aiogram 

####Запуск  
Файл запуска бота - app.py  
Перед запуском нужно настроить переменные среды: 
предварительно корректируем файл .env.example 
и переименовываем его в .env

####  Настройка локалихаций
В терминале окрудения выолняем: 
* pybabel extract . -o locales/testbot.pot
Это командой мы собрали все текста для перевода, обернутые в _('Text'')

* pybabel init -i locales/testbot.pot -d data/locales -D testbot -l en
pybabel init -i locales/testbot.pot -d data/locales -D testbot -l ru
Этими командами нарезаем файлы для переводов на различные языки
В папке с языком по умолчанию никаких правок вносить не нужно. 

* Далее вручную делаем перевод в файлах .po

* pybabel compile -d data/locales -D testbot
Это командой компилим переводы в файлы типа .mo


Процесс обновления локалей следдующий
* pybabel extract . -o locales/testbot.pot
* pybabel update -d locales -D testbot -i locales/testbot.pot 
* Ручные правки файлов .po
* pybabel compile -d data/locales -D testbot

#### Некоторые особенности
1) По дефолту всегда будет устанавливаться та локаль под которую вы писали бота. 
   Писали на ресском  - будет на русском. Все альтернативные языки будут устанавливаться в зависимости от данных в хранилке. 
   Если в хранилке пусто, то в нее полетит локаль бота по умолчанию.
   
```python
class MultiLang(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]):
        user: types.User = types.User.get_current()
        if LANG_STORAGE.get(user.id) is None:
            LANG_STORAGE[user.id] = "ru"
        *_, data = args
        language = data['locale'] = LANG_STORAGE[user.id]
        return language
```

Тут вообще зависит от настройки вашей мидлы. Но дефолтное значение оно всегда есть и будет. 
После смены языка диалоги продолжнаться сразу на новом языке. 

2) Относительно клавиатур ситуация следующая.  
   **Инлайн клавиатуры** - будут выводиться на измененном языке в следующих сообщениях. Ранее выведенные - останутся на прежнем языке.  
   **Реплай клавиатуры** - поведение аналогичное. Исключение составляют только main (статические) клавиатуры (которые у вас болтаются постоянно под вводом сообщения). Их значения обновится только после рестарта бота со стороны клиента.  
   

   Обновление клавиатур после смены языка может не работать. 
   Решается с помощью ```_ = i18n.lazy_gettext  ```  
   В любом случае main keyboards обновятся только после рестарта


3) Смена языка для команд бота работет следующим образом. 
К примеру on_startup бота вы цепляете функцию определения команд: 

```python
async def set_default_commands(dp):
    data = [
        # Commands in private chats (English and Russian)
        (
            [
                types.BotCommand(command="start", description="Bot start"),
                types.BotCommand(command="help", description="Show help"),
                types.BotCommand(command="lang", description=«Сhoose language")
            ],
            types.BotCommandScopeAllPrivateChats(),
            "en"
        ),
        (
            [
                types.BotCommand(command="start", description="Запуск бота"),
                types.BotCommand(command="help", description="Вывести справку"),
                types.BotCommand(command="lang", description="Выбрать язык")
            ],
            types.BotCommandScopeAllPrivateChats(),
            "ru"
        ),
    ]
    for commands_list, commands_scope, language in data:
        await dp.bot.set_my_commands(commands=commands_list, scope=commands_scope, language_code=language)
    logging.info("Базовые команды успешно установлены")
```

Вне зависимости от того какая локаль для вашего пользователя прописана в хранилке или вернется мидлой - язык будет устанавливаться исходя из настроек вашего телеграм клиента.  

Переопределение значений не поможет, об этом нам гласит core документация:  
*Determining list of commands
The following algorithm is used to determine the list of commands for a particular user viewing the bot menu. The first list of commands which is set is returned*