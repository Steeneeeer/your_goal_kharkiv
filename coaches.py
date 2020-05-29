from telegram_bot_pagination import InlineKeyboardPaginator


coaches_list = {1: ("Константин Остапенко", "+380675729936" ),
                2: ("Феликс Морозов", "номер телефона"),
                3: ("Андрей Николаевич Лупандин", "номер телефона"),
                4: ("Артём Александрович Кобиков", "номер телефона"),
                5: ("Валерий Скребела", "номер телефона"),
}


class MyPaginator(InlineKeyboardPaginator):
    current_page_label = '-{}-'


