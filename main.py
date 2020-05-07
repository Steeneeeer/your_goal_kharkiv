import telebot
import config
import phrases as ph
from keyboards import main_keyboard
from keyboards import schedule_keyboard
from telegram_bot_pagination import InlineKeyboardPagination


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    return bot.send_message(message.chat.id, ph.START_MESSAGE, reply_markup=main_keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'schedule')
def callback_inline(call):
    return bot.send_message(call.message.chat.id, ph.SCHEDULE_MESSAGE, reply_markup=schedule_keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'address')
def callback_inline(call):
    bot.send_message(call.message.chat.id, ph.ADDRESS_MESSAGE)
    bot.send_photo(call.message.chat.id, 'https://www.instagram.com/p/BxHSeUNgRtR/')
    bot.send_location(call.message.chat.id, 49.9661396, 36.3217929)


@bot.callback_query_handler(func=lambda call: call.data == 'prices')
def callback_inline(call):
    bot.send_message(call.message.chat.id, ph.PRICES_MESSAGE)


@bot.callback_query_handler(func=lambda call: call.data == 'ice_info')
def callback_inline(call):
    bot.send_message(call.message.chat.id, ph.ICE_INFO_MESSAGE)


@bot.callback_query_handler(func=lambda call: call.data == 'coaches')
def callback_inline(call):
    bot.send_message(call.message.chat.id, ph.COACHES_MESSAGE)


@bot.callback_query_handler(func=lambda call: call.data == 'ask')
def callback_inline(call):
    bot.send_message(call.message.chat.id, ph.ASK_MESSAGE)


bot.polling(none_stop=True)
