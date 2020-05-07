from telebot import types

main_keyboard = types.InlineKeyboardMarkup(row_width=1)

prices = types.InlineKeyboardButton("Цены", callback_data="prices")
schedule = types.InlineKeyboardButton("Расписание", callback_data="schedule")
address = types.InlineKeyboardButton("Адрес", callback_data="address")
ice_info = types.InlineKeyboardButton("Информация по льду", callback_data="ice_info")
coaches = types.InlineKeyboardButton("Тренера", callback_data="coaches")
ask = types.InlineKeyboardButton("Задать вопрос", callback_data="ask")

main_keyboard.add(prices, schedule, address, ice_info, coaches, ask)

schedule_keyboard = types.InlineKeyboardMarkup()

url_button_calendar = types.InlineKeyboardButton(text="Посмотреть календарь",
                                                 url="https://calendar.google.com/calendar/embed?src=hvpn2gg82bi7pfjaag62slv5i8%40group.calendar.google.com&ctz=Europe%2FKiev")
url_button_instagram = types.InlineKeyboardButton(text="Посмотреть календарь",
                                                  url="https://www.instagram.com/your_goal.kharkov/")
schedule_keyboard.add(url_button_calendar, url_button_instagram)