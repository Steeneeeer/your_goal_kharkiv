import os
import logging

import telebot

from config import BASE_DIR
from bot_init import bot

FILE_TO_SAVE = os.path.join(BASE_DIR, 'users.txt')


if not os.path.exists(FILE_TO_SAVE):
    with open(FILE_TO_SAVE, 'w') as f:
        pass


def add_user(user_id):
    if str(user_id) in read_users():
        return
    with open(FILE_TO_SAVE, 'a') as f:
        print(user_id, file=f)


def read_users():
    with open(FILE_TO_SAVE, 'r') as f:
        users = f.read().split()
    return users


def send_messages(users, message, parse_mode=None, reply_markup=None):
    for user in users:
        try:
            bot.send_message(chat_id=user, text=message, parse_mode=parse_mode, reply_markup=reply_markup)
        except telebot.apihelper.ApiException:
            logging.error(f"Message to user {user} was not sent")


@bot.message_handler(commands=['sending_secret_message'])
def send_message(message):
    message_text = message.text[message.text.find(' '):]
    users = read_users()
    send_messages(users, message_text)
