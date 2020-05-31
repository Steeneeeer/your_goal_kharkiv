from telebot import types

main_keyboard = types.ReplyKeyboardMarkup(row_width=2)

prices = types.KeyboardButton("Цены")
schedule = types.KeyboardButton("Расписание")
address = types.KeyboardButton("Адрес")
ice_info = types.KeyboardButton("Информация по льду")
coaches = types.KeyboardButton("Тренера")
ask = types.KeyboardButton("Задать вопрос")

main_keyboard.add(prices, schedule, address, ice_info, coaches, ask)


schedule_keyboard = types.InlineKeyboardMarkup()

url_button_calendar = types.InlineKeyboardButton(text="Посмотреть календарь",
                                                 url="https://calendar.google.com/calendar/embed?src=hvpn2gg82bi7pfjaag62slv5i8%40group.calendar.google.com&ctz=Europe%2FKiev")
url_button_instagram = types.InlineKeyboardButton(text="Инстаграм",
                                                  url="https://www.instagram.com/your_goal.kharkov/")

schedule_keyboard.add(url_button_calendar, url_button_instagram)