import telebot
import config
from telebot import types
import phrases as ph


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    prices = types.InlineKeyboardButton("Цены", callback_data= "prices")
    schedule = types.InlineKeyboardButton("Расписание", callback_data="schedule")
    addres = types.InlineKeyboardButton("Адресс", callback_data="addres")
    ice_info = types.InlineKeyboardButton("Информация по льду", callback_data="ice_info")
    coaches = types.InlineKeyboardButton("Тренера", callback_data="coaches")
    ask = types.InlineKeyboardButton("Задать вопрос", callback_data="ask")

    markup.add(prices, schedule, addres, ice_info, coaches, ask)

    return bot.send_message(message.chat.id, ph.START_MESSAGE, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'prices':
                bot.send_message(call.message.chat.id, ph.PRICES_MESSAGE)
            elif call.data == 'schedule':
                bot.send_message(call.message.chat.id, ph.SCHEDULE_MESSAGE)
            elif call.data == 'addres':
                bot.send_message(call.message.chat.id, ph.ADDRES_MESSAGE)
            elif call.data == 'ice_info':
                bot.send_message(call.message.chat.id, ph.ICE_INFO_MESSAGE)
            elif call.data == 'coaches':
                bot.send_message(call.message.chat.id, ph.COACHES_MESSAGE)
            elif call.data == 'ask':
                bot.send_message(call.message.chat.id, ph.ASK_MESSAGE)
            else:
                bot.send_message(message.chat.id, "Бот не отвечает на текстовые сообщения")
    except Exeption as e:
        print(repr(e))

bot.polling(none_stop=True)

# @bot.message_handler(commands=['schedule'])
# def schedule(message):
#     keyboard = types.InlineKeyboardMarkup()
#     url_button = types.InlineKeyboardButton(text="Расписание", url="https://calendar.google.com/calendar/embed?src=hvpn2gg82bi7pfjaag62slv5i8%40group.calendar.google.com&ctz=Europe%2FKiev")
#     keyboard.add(url_button)
#     url_button = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/your_goal.kharkov/")
#     keyboard.add(url_button)
#     bot.send_message(message.chat.id, ph.SCHEDULE_MESSAGE, reply_markup=keyboard)

# @bot.message_handler(content_types=["text"])
# def prices(message):
#     callback_button = types.InlineKeyboardButton(text="Цены", callback_data= "prices")
#     markup.add(callback_button)
#     bot.send_message(message.chat.id, ph.PRICES_MESSAGE, reply_markup=keyboard)




