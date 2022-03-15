Урок 1 (test.py)

Изучаю tg bot, хочу узнать машину состояний
по видео
https://www.youtube.com/watch?v=FRUKYZtOaSM&t=37s

Урок 2 Архитектура проекта
 
 Создал папку data в ней config.py (перечислены id админов, вызывается токен из .env)
 $ pip install python-dotenv
 -вне папки data создал фаил .env (здесь хранится токен моего бота)
 -создал папку handler, в ней папку users (также здесь буду создавать файлы для других команд: hello.py, help.py), в ней start.py ()
 -loader.py (не совсем пойму, он вызывает BOT_TOKEN из config )
-созд app.py (это главный фаил, в нем я вызываю ф-ции из utils. Всегда запускаю его!)
- созд папку utils, в ней notify_admins.py (будет отправлять сообщение в tg всем админам из configa) & set_bot_commands.py (в utils) (причем, здесь пишется описание для контекстного меню, этих функций может не быть в users, а в users, могут быть рабочие функции и не быть здесь )
-коррект app.py
-коррект start.py ()
-коррект __init__.py (in users)
-коррект __init__.py (in handlers)


-созд help.py (+ в __init__)
-созд hello.py (+ в __init__) +(set_bot_commands.py)


*****************
Урок 3 (меню, обычные кнопки)
-requirements.txt *
-созд menu.py(in handlers/users/menu.py)
-созд keyboards, default, keyboard_menu.py (keyboards/default/keyboard_menu.py), 
-созд __init__.py (in keyboards/default/)
-коррект menu.py & __init__.py( in users!) (я от себя откорект set_bot_commands.py)
- запускаю, команда /menu и вижу кнопки

пишу хэндлеры, которые будут ловить сообщения от кнопок
-созд buttons.py (in users), коррект __init__.py(users!)
-запускаю, вижу ответы на нажатия цифр на клаве(в тг боте)

-созд error.py, коррект __init__.py(users!)
- запуск, проверка

-созд test.py (in users)
-созд keyboard_test.py (in keyboards/default)
-коррект __init__.py(in keyboards/default)
-коррeкт test.py (in users)
-коррект __init__.py (in users)
-запускаю, при нажатии "Любой текст", выводится сообщение (из test.py)" и кнопка "/menu"


********************
Урок 4 (inlain button) кнопки, которые прикреплены к сообщениям
-коррект keyboard_menu.py ( KeyboardButton(text="Инлайн меню"),
            KeyboardButton(text="Любой текст"),
            KeyboardButton(text="Лайк"),)

-cозд inlain_menu.py (in users)
-созд inlain & inlain_kb_menu.py (in keyboards)
- созд __init__.py (in inlain)
-корркт inlain_menu.py
-коррект __init__.py (in users)
-запускаем, проверяю команы:
*/menu -> кнопки внизу, 
*Инлайн меню(на клаве внизу) -> выводится инлайн меню, 
команды на инлайн клаве:
*Сообщение -> нет реакции,
*alert -> нет реакции,
*Ссылка -> переход по ссылке

-допишу норм реакцию на остальные кнопки инлайин меню
- корркт inlain_menu.py (in users) (@dp.callback_query_handler(text="Сообщение") & @dp.callback_query_handler(text="alert"))
-запускаю:
*Инлайн меню(на клаве внизу) -> выводится инлайн меню,
*Сообщение (на инлайн клаве) -> Кнопки заменены (from inline_menu.py)+ заменяет клавиатуру (внизу только "/menu"),
*/menu -> Выбери число из меню ниже + клава внизу,
*Инлайн меню(на клаве внизу) -> выводится инлайн меню,
*alert -> выводится временное сообщение "Кнопки заменены"

-добавлю еще кнопку
-inlain_kb_menu.py (in keyboard) (InlineKeyboardButton(text="Заменить кнопки меню", callback_data="кнопки2"))
-коррект inlain_menu.py (@dp.callback_query_handler(text="Кнопки2"))
-созд inline_kb_menu2.py (in keyboard/inline)
-коррект __init__ (in inlain)
-импорт в imlain_menu.py
-тестирую 

********************
Урок 5 (Машина состояний)
- в loader.py создаю хранилище оперативной памяти
- созд директорию states
- в ней test.py & __init__.py
- create handlers/users/register.py
- зарегать в __init.py__ (handlers/users/)
- откорект set_bot_commands.py








 




