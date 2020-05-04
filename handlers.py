from bot import BOT
import your_goal_kharkiv.phrases as ph

import telebot
from .models import Chat, TgUser


TOKEN = [1109214579:AAHpGYeD5Y1Go9eCnlC0QkGANKU00WPQJm0]

def user_exists(tg_id):
    return TgUser.objects.filter(tg_id=tg_id).exists()


@BOT.message_handler(commands=['start'])
def cmd_start(message):
    if not user_exists(message.chat.id):
        tg_id = message.chat.id
        first_name = message.chat.first_name
        username = message.chat.username
        TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
    return BOT.reply_to(message, ph.START_MESSAGE)

@BOT.message_handler(commands=['prices'])
def cmd_start(message):
    if not user_exists(message.chat.id):
        tg_id = message.chat.id
        first_name = message.chat.first_name
        username = message.chat.username
        TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
    return BOT.reply_to(message, ph.PRICES_MESSAGE)


@BOT.message_handler(commands=['schedule'])
def cmd_start(message):
    if not user_exists(message.chat.id):
        tg_id = message.chat.id
        first_name = message.chat.first_name
        username = message.chat.username
        TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
    return BOT.reply_to(message, ph.SCHEDULE_MESSAGE)


@BOT.message_handler(commands=['addres'])
def cmd_start(message):
    if not user_exists(message.chat.id):
        tg_id = message.chat.id
        first_name = message.chat.first_name
        username = message.chat.username
        TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
    return BOT.reply_to(message, ph.ADDRES_MESSAGE)


@BOT.message_handler(commands=['ice_info'])
def cmd_start(message):
    if not user_exists(message.chat.id):
        tg_id = message.chat.id
        first_name = message.chat.first_name
        username = message.chat.username
        TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
    return BOT.reply_to(message, ph.ICE_INFO_MESSAGE)

@BOT.message_handler(commands=['coaches'])
def cmd_start(message):
    if not user_exists(message.chat.id):
        tg_id = message.chat.id
        first_name = message.chat.first_name
        username = message.chat.username
        TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
    return BOT.reply_to(message, ph.COACHES_MESSAGE)


@BOT.message_handler(commands=['ask'])
def cmd_start(message):
    if not user_exists(message.chat.id):
        tg_id = message.chat.id
        first_name = message.chat.first_name
        username = message.chat.username
        TgUser.objects.create(tg_id=tg_id, first_name=first_name, username=username)
    return BOT.reply_to(message, ph.ASK_MESSAGE)

