from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def bonus_keyboards():
    """Клавиатура для выбора города"""
    bonus_keyboards = InlineKeyboardMarkup()
    top_pard = InlineKeyboardButton(text='Добролюбова, д.4 (Верхняя часть города)', callback_data='top_pard')
    bottom_part = InlineKeyboardButton(text='проспект Ильича, д.25 (Нижняя часть города)', callback_data='bottom_part')
    bonus_keyboards.row(top_pard)
    bonus_keyboards.row(bottom_part)
    return bonus_keyboards


def top_kub_keyboards():
    """Клавиатура для выбора города"""
    top_kub_keyboards = InlineKeyboardMarkup()
    top_kub = InlineKeyboardButton(text='🎲', callback_data='top_kub')
    top_kub_keyboards.row(top_kub)
    return top_kub_keyboards


def bottom_kub_keyboards():
    """Клавиатура для выбора города"""
    bottom_kub_keyboards = InlineKeyboardMarkup()
    bottom_kub = InlineKeyboardButton(text='🎲', callback_data='bottom_kub')
    bottom_kub_keyboards.row(bottom_kub)
    return bottom_kub_keyboards


if __name__ == '__main__':
    bonus_keyboards()
