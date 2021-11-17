### Реализация мультиязычности в aiogram 

####Запуск  
app.py 
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

#### Проблемы
1) обновление клавиатур после смены языка
решается с помощью _ = i18n.lazy_gettext  
   В любом случае main keyboards обновятся только после рестарта
   
2) Обновление описания зарегистрированных команд 
Вроде как можно решить через BotCommandScopeChat, но для определения требуется chat.id  
   Который при старте хз откуда брать (в диспетчере его нет)