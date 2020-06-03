from telegram_bot_pagination import InlineKeyboardPaginator
from collections import namedtuple

Coach = namedtuple("Coach", ("photo_id", "text"))


coaches_list = {
    1: Coach("AgACAgIAAxkBAAIBtl7VWY5BQa5FtHqXIn5Z0z5z31tMAALdtDEbDwABqErSc_Bkurg39d3j-ZQuAAMBAAMCAANtAAMFTgACGQQ",
             "Константин Остапенко +380675729936"),
    2: Coach("AgACAgIAAxkBAAIBtl7VWY5BQa5FtHqXIn5Z0z5z31tMAALdtDEbDwABqErSc_Bkurg39d3j-ZQuAAMBAAMCAANtAAMFTgACGQQ",
             "Феликс Морозов номер телефона"),
    3: Coach("AgACAgIAAxkBAAIBt17VWibnYs0jY2ViaQjeBbQp8unDAAJ_rTEbDwABsEoufXcs6fCWemCa35MuAAMBAAMCAANtAAOLGQEAARkE",
             "Андрей Николаевич Лупандин номер телефона"),
    4: Coach("AgACAgIAAxkBAAIBt17VWibnYs0jY2ViaQjeBbQp8unDAAJ_rTEbDwABsEoufXcs6fCWemCa35MuAAMBAAMCAANtAAOLGQEAARkE",
             "Артём Александрович Кобиков номер телефона"),
    5: Coach("AgACAgIAAxkBAAIBt17VWibnYs0jY2ViaQjeBbQp8unDAAJ_rTEbDwABsEoufXcs6fCWemCa35MuAAMBAAMCAANtAAOLGQEAARkE",
             "Валерий Скребела номер телефона"),
    }


class MyPaginator(InlineKeyboardPaginator):
    current_page_label = '-{}-'
