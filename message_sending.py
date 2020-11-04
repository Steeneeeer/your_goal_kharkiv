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
    for user_id in users:
        try:
            bot.send_message(chat_id=user_id, text=message, parse_mode=parse_mode, reply_markup=reply_markup)
        except telebot.apihelper.ApiException:
            logging.error(f"Message to user {user_id} was not sent")


def send_images(users, image, caption, parse_mode=None, reply_markup=None):
    for user_id in users:
        try:
            bot.send_photo(user_id, image, caption=caption, parse_mode=parse_mode, reply_markup=reply_markup)
        except telebot.apihelper.ApiException:
            logging.error(f"Message to user {user_id} was not sent")


def send_videos(users, video_id, caption, parse_mode=None, reply_markup=None):
    for user_id in users:
        try:
            bot.send_video(user_id, video_id, caption=caption, parse_mode=parse_mode, reply_markup=reply_markup)
        except telebot.apihelper.ApiException:
            try:
                bot.send_animation(user_id, video_id, caption=caption, parse_mode=parse_mode, reply_markup=reply_markup)
            except telebot.apihelper.ApiException as e:
                logging.error(e.__traceback__)
            logging.error(f"Message to user {user_id} was not sent")


@bot.message_handler(commands=['sending_secret_message'])
def send_message(message):
    message_text = message.text[message.text.find(' '):]
    users = read_users()
    send_messages(users, message_text)


@bot.message_handler(commands=['sending_secret_image'])
def cmd_send_image(message):
    bot.send_message(message.chat.id, text="Send me an image to mailing")
    bot.register_next_step_handler(message, mail_image)


def mail_image(message: telebot.types.Message):
    if message.text == "cancel":
        return bot.send_message(message.chat.id, "Ok bro")
    elif not message.photo:
        bot.send_message(message.chat.id, "Please, send a photo")
        return bot.register_next_step_handler(message, mail_image)
    users = read_users()
    photo = message.photo[0].file_id
    caption = message.caption
    send_images(users, photo, caption)


@bot.message_handler(commands=['sending_secret_video'])
def cmd_send_video(message):
    bot.send_message(message.chat.id, text="Send me a video to mailing")
    bot.register_next_step_handler(message, mail_video)


def mail_video(message: telebot.types.Message):
    if message.text == "cancel":
        return bot.send_message(message.chat.id, "Ok bro")
    elif not message.video and not message.animation:
        bot.send_message(message.chat.id, "Please, send a video")
        return bot.register_next_step_handler(message, mail_video)
    users = read_users()
    video = message.video or message.animation
    video_id = video.file_id
    caption = message.caption
    send_videos(users, video_id, caption)
