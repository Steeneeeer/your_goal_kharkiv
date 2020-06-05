import telebot

joined_file = open("C:\\Users\\Kastet\\Desktop\\users_database.txt", "r")
joined_users = set()
for line in joined_file:
    joined_users.add(line.strip())
    joined_file.close()

bot = telebot.TeleBot("1109214579:AAHpGYeD5Y1Go9eCnlC0QkGANKU00WPQJm0")


@bot.message_handler(commands=['start'])
def get_id(message):
    if not str(message.chat.id) in joined_users:
        joined_file = open("C:\\Users\\Kastet\\Desktop\\users_database.txt", "a")
        joined_file.write(str(message.chat.id) + '\n')
        joined_users.add(message.chat.id)


@bot.message_handler(commands=['sending_secret_message'])
def send_message(message):
    for user in joined_users:
        bot.send_message(user, message.text[message.text.find(' '):])
