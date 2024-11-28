from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loguru import logger


def city_selection_keyboard():
    """Клавиатура выбора города"""

    try:
        nizhniy_novgorod_button = [
            [
                InlineKeyboardButton(text='Нижний Новгород', callback_data='nizhniy_novgorod_button'),
            ],
        ]
        city_selection_key = InlineKeyboardMarkup(inline_keyboard=nizhniy_novgorod_button)
        return city_selection_key
    except Exception as e:
        logger.error(f"Ошибка: {e}")


def greeting_keyboards():
    """Клавиатуры поста приветствия 🎲"""

    try:
        keyboards_greeting = [
            [
                InlineKeyboardButton(text='Получить бонус', callback_data='get_a_bonus'),
                InlineKeyboardButton(text='📇 О нас', callback_data='reference')
            ],
        ]
        keyboards_greeting = InlineKeyboardMarkup(inline_keyboard=keyboards_greeting)
        return keyboards_greeting
    except Exception as e:
        logger.error(f"Ошибка: {e}")


if __name__ == '__main__':
    greeting_keyboards()
    city_selection_keyboard()
