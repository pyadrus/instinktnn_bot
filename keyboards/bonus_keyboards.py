from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def bonus_keyboards():
    """Клавиатура для выбора города"""
    bonus_keyboards = InlineKeyboardMarkup()
    top_pard = InlineKeyboardButton(text='Добролюбова, д.4 (Верхняя часть города)',
                                    callback_data='dobrolyudova')
    bottom_part = InlineKeyboardButton(text='проспект Ильича, д.25 (Нижняя часть города)',
                                       callback_data='Ilyich_button')
    bonus_keyboards.row(top_pard)
    bonus_keyboards.row(bottom_part)
    return bonus_keyboards


def dobrolyudova_keyboards():
    """Клавиатура 🎲"""
    top_kub_keyboards = InlineKeyboardMarkup()
    top_kub = InlineKeyboardButton(text='🎲', callback_data='dobrolyudova_kub')
    top_kub_keyboards.row(top_kub)
    return top_kub_keyboards


def ilyich_keyboards():
    """Клавиатура 🎲"""
    bottom_kub_keyboards = InlineKeyboardMarkup()
    bottom_kub = InlineKeyboardButton(text='🎲', callback_data='ilyich_kub')
    bottom_kub_keyboards.row(bottom_kub)
    return bottom_kub_keyboards


if __name__ == '__main__':
    bonus_keyboards()
