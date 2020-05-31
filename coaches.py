from telegram_bot_pagination import InlineKeyboardPaginator
from collections import namedtuple

Coach = namedtuple("Coach", ("photo_id", "text"))


coaches_list = {
    1: Coach("AgACAgIAAxkBAAJVfl7UDypKtT_7RBwkYj44S5Ox5kV2AALFrjEb_wehSsTzCnLKNZ79jyq8ki4AAwEAAwIAA20AA1GzAgABGQQ",
             "Константин Остапенко +380675729936"),
    2: Coach("AgACAgIAAxkBAAJVhV7UE4BJMVAaSt-K3iIsJOkIvifQAALNrjEb_wehSsxyscaFIlmJgXzjkS4AAwEAAwIAA20AAx6kAgABGQQ",
             "Феликс Морозов номер телефона"),
    3: Coach("AgACAgIAAxkBAAJVfl7UDypKtT_7RBwkYj44S5Ox5kV2AALFrjEb_wehSsTzCnLKNZ79jyq8ki4AAwEAAwIAA20AA1GzAgABGQQ",
             "Андрей Николаевич Лупандин номер телефона"),
    4: Coach("AgACAgIAAxkBAAJVfl7UDypKtT_7RBwkYj44S5Ox5kV2AALFrjEb_wehSsTzCnLKNZ79jyq8ki4AAwEAAwIAA20AA1GzAgABGQQ",
             "Артём Александрович Кобиков номер телефона"),
    5: Coach("AgACAgIAAxkBAAJVfl7UDypKtT_7RBwkYj44S5Ox5kV2AALFrjEb_wehSsTzCnLKNZ79jyq8ki4AAwEAAwIAA20AA1GzAgABGQQ",
             "Валерий Скребела номер телефона"),
    }


class MyPaginator(InlineKeyboardPaginator):
    current_page_label = '-{}-'
