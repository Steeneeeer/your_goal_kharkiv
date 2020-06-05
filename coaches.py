from telegram_bot_pagination import InlineKeyboardPaginator
from collections import namedtuple

Coach = namedtuple("Coach", ("photo_id", "text"))


coaches_list = {
    1: Coach("AgACAgIAAxkBAAICG17Y2vT5_H4Tr9jNyU3eTgccASEKAAL9sDEbeInJSvlrJZx0wlsmUJl9ki4AAwEAAwIAA20AA6A_AgABGgQ",
             "Константин Остапенко +380675729936"),
    2: Coach("AgACAgIAAxkBAAICI17Y3SSWjvfFTaVQzp1ApvkJQ1piAAIXsTEbeInJSvimn_b33n0VjsvDki4AAwEAAwIAA3kAA7zYAgABGgQ",
             "Феликс Морозов +380953977260"),
    3: Coach("AgACAgIAAxkBAAICJV7Y3ZplUdukos_VLD2DAzfpv6eOAAIZsTEbeInJSr93zmFLrXzxPgGUlS4AAwEAAwIAA3kAA5cEAAIaBA",
             "Андрей Николаевич Лупандин +380951666515"),
    4: Coach("AgACAgIAAxkBAAICJF7Y3VTa8h44o989PTaMgSGvb6XQAAIYsTEbeInJSltqZSgtJ6C1BoLZky4AAwEAAwIAA3kAA6c4AQABGgQ",
             "Артём Александрович Кобиков +380501900989"),
    5: Coach("AgACAgIAAxkBAAICHF7Y28vVpLeajlfr_P_U-ak58f3iAAIVsTEbeInJSmqXt5xCRnTZq9UTlS4AAwEAAwIAA3gAA6YEAAIaBA",
             "Валерий Скребела +380673661328"),
    }


class MyPaginator(InlineKeyboardPaginator):
    current_page_label = '-{}-'
