from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loguru import logger


def bonus_keyboards():
    """Клавиатура для выбора города"""

    try:
        bonus_key = [
            [InlineKeyboardButton(text='Добролюбова, д.4 (Верхняя часть города)',
                                  callback_data='dobrolyudova'), ],
            [InlineKeyboardButton(text='проспект Ильича, д.25 (Нижняя часть города)',
                                  callback_data='Ilyich_button')],
        ]
        bonus_keyboards = InlineKeyboardMarkup(inline_keyboard=bonus_key)
        return bonus_keyboards
    except Exception as e:
        logger.error(f"Ошибка: {e}")


def dobrolyudova_keyboards():
    """Клавиатура 🎲"""

    try:
        top_kub = [
            [InlineKeyboardButton(text='🎲', callback_data='dobrolyudova_kub')]
        ]
        top_kub_keyboards = InlineKeyboardMarkup(inline_keyboard=top_kub)
        return top_kub_keyboards
    except Exception as e:
        logger.error(f"Ошибка: {e}")


def ilyich_keyboards():
    """Клавиатура 🎲"""

    try:
        top_kub = [
            [InlineKeyboardButton(text='🎲', callback_data='ilyich_kub')]
        ]
        top_kub_keyboards = InlineKeyboardMarkup(inline_keyboard=top_kub)
        return top_kub_keyboards
    except Exception as e:
        logger.error(f"Ошибка: {e}")


if __name__ == '__main__':
    bonus_keyboards()
