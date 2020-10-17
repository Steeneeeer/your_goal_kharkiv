from telebot import types

main_keyboard = types.ReplyKeyboardMarkup(row_width=2)

prices_button = types.KeyboardButton("Цены")
schedule_button = types.KeyboardButton("Расписание")
address_button = types.KeyboardButton("Адрес")
ice_info_button = types.KeyboardButton("Информация по льду")
coaches_button = types.KeyboardButton("Тренера")
franchise_button = types.KeyboardButton("Сотрудничество")
ask_button = types.KeyboardButton("Задать вопрос")


main_keyboard.add(prices_button, schedule_button, address_button, ice_info_button, coaches_button, franchise_button, ask_button)


schedule_keyboard = types.InlineKeyboardMarkup()

url_button_calendar = types.InlineKeyboardButton(text="Посмотреть календарь",
                                                 url="https://calendar.google.com/calendar/embed?src=hvpn2gg82bi7pfjaag62slv5i8%40group.calendar.google.com&ctz=Europe%2FKiev")
url_button_instagram = types.InlineKeyboardButton(text="Инстаграм",
                                                  url="https://www.instagram.com/your_goal.kharkov/")

schedule_keyboard.add(url_button_calendar, url_button_instagram)
