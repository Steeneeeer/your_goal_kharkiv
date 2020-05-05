import telebot
import config
from telebot import types
import phrases as ph


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Цены", callback_data= "prices"))
    markup.add(types.InlineKeyboardButton("Расписание", callback_data="schedule"))
    markup.add(types.InlineKeyboardButton("Адресс", callback_data="addres"))
    markup.add(types.InlineKeyboardButton("Информация по льду", callback_data="ice_info"))
    markup.add(types.InlineKeyboardButton("Тренера", callback_data="coached"))
    markup.add(types.InlineKeyboardButton("Задать вопрос", callback_data="ask"))
    return bot.send_message(message.chat.id, ph.START_MESSAGE, reply_markup=markup)

bot.polling(none_stop=True)


#@BOT.message_handler(commands=['start'])
# def cmd_start(message):
#     if not user_exists(message.chat.id):
#         tg_id = message.chat.id
#         first_name = message.chat.first_name
#         username = message.chat.username
#         TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
#     return BOT.reply_to(message, ph.START_MESSAGE)
#
# @BOT.message_handler(commands=['prices'])
# def cmd_start(message):
#     if not user_exists(message.chat.id):
#         tg_id = message.chat.id
#         first_name = message.chat.first_name
#         username = message.chat.username
#         TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
#     return BOT.reply_to(message, ph.PRICES_MESSAGE)
#
#
# @BOT.message_handler(commands=['schedule'])
# def cmd_start(message):
#     if not user_exists(message.chat.id):
#         tg_id = message.chat.id
#         first_name = message.chat.first_name
#         username = message.chat.username
#         TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
#     return BOT.reply_to(message, ph.SCHEDULE_MESSAGE)
#
#
# @BOT.message_handler(commands=['addres'])
# def cmd_start(message):
#     if not user_exists(message.chat.id):
#         tg_id = message.chat.id
#         first_name = message.chat.first_name
#         username = message.chat.username
#         TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
#     return BOT.reply_to(message, ph.ADDRES_MESSAGE)
#
#
# @BOT.message_handler(commands=['ice_info'])
# def cmd_start(message):
#     if not user_exists(message.chat.id):
#         tg_id = message.chat.id
#         first_name = message.chat.first_name
#         username = message.chat.username
#         TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
#     return BOT.reply_to(message, ph.ICE_INFO_MESSAGE)
#
# @BOT.message_handler(commands=['coaches'])
# def cmd_start(message):
#     if not user_exists(message.chat.id):
#         tg_id = message.chat.id
#         first_name = message.chat.first_name
#         username = message.chat.username
#         TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
#     return BOT.reply_to(message, ph.COACHES_MESSAGE)
#
#
# @BOT.message_handler(commands=['ask'])
# def cmd_start(message):
#     if not user_exists(message.chat.id):
#         tg_id = message.chat.id
#         first_name = message.chat.first_name
#         username = message.chat.username
#         TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
#     return BOT.reply_to(message, ph.ASK_MESSAGE)

