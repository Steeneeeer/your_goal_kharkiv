from telegram_bot_pagination import InlineKeyboardPaginator


coaches_list = {1: ("Остапенко Константин", "+380675729936" ),
                2: ("Второй тренер", "номер телефона"),
                3: ("Третий тренер", "номер телефона"),
                4: ("Чётвёртый тренер", "номер телефона"),
                5: ("Пятый тренер", "номер телефона"),
                6: ("Шестой тренер", "номер телефона"),
}


class MyPaginator(InlineKeyboardPaginator):
    previous_page_label = '<'
    current_page_label = '-{}-'
    next_page_label = '>'

    # paginator = InlineKeyboardPaginator(
    #     len(coaches_list),
    #     current_page=1,
    #     data_pattern='coaches_list#{page}'
    # )


# bot.send_message(
#     chat_id,
#     text,
#     reply_markup=paginator.markup,
# )
