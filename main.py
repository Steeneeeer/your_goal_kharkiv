import telebot
import config
import phrases as ph
from keyboards import main_keyboard
from keyboards import schedule_keyboard, schedule_button, address_button, prices_button, ice_info_button, coaches_button, ask_button
import coaches as pg

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    return bot.send_message(message.chat.id, ph.START_MESSAGE, reply_markup=main_keyboard)


@bot.message_handler(func=lambda message: message.text == schedule_button.text)
def schedule(message):
    return bot.send_message(message.chat.id, ph.SCHEDULE_MESSAGE, reply_markup=schedule_keyboard)


@bot.message_handler(func=lambda message: message.text == address_button.text)
def address(message):
    bot.send_message(message.chat.id, ph.ADDRESS_MESSAGE)
    bot.send_photo(message.chat.id, 'https://www.instagram.com/p/BxHSeUNgRtR/')
    bot.send_location(message.chat.id, 49.9661396, 36.3217929)


@bot.message_handler(func=lambda message: message.text == prices_button.text)
def prices(message):
    bot.send_message(message.chat.id, ph.PRICES_MESSAGE)


@bot.message_handler(func=lambda message: message.text == ice_info_button.text)
def ice_info(message):
    bot.send_message(message.chat.id, ph.ICE_INFO_MESSAGE)


@bot.message_handler(func=lambda message: message.text == coaches_button.text)
def coaches_list_callback(message):
    message_text, photo_id, markup = generate_pagination_messsage()
    bot.send_photo(message.chat.id, photo_id, message_text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.split('#')[0] == 'coaches_list')
def coaches_list_pagination(call):
    page_number = int(call.data.split('#')[1])
    current_page = int(call.data.split('#')[-1])
    if page_number == current_page:
        return bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Current coach")

    message_text, photo_id, markup = generate_pagination_messsage(page_number)

    media = telebot.types.InputMedia('photo', photo_id, message_text)

    bot.edit_message_media(media, call.message.chat.id, call.message.message_id, reply_markup=markup)


def generate_pagination_messsage(current_page=1):
    paginator = pg.MyPaginator(
        len(pg.coaches_list),
        current_page=current_page,
        data_pattern='coaches_list#{page}#current_page#%d' % current_page
    )
    coach = pg.coaches_list[current_page]
    message = coach.text
    photo_id = coach.photo_id
    return message, photo_id, paginator.markup


@bot.message_handler(func=lambda message: message.text == ask_button.text)
def ask(message):
    bot.send_message(message.chat.id, ph.ASK_MESSAGE)


bot.polling(none_stop=True)
