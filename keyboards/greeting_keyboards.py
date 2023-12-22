from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def greeting_keyboards():
    """Клавиатуры поста приветствия 🎲"""
    keyboards_greeting = InlineKeyboardMarkup()
    get_a_bonus = InlineKeyboardButton(text='Получить бонус', callback_data='get_a_bonus')
    reference_keyboard = InlineKeyboardButton(text='📇 О нас', callback_data='reference')  # Контакты
    keyboards_greeting.row(reference_keyboard, get_a_bonus)
    
    return keyboards_greeting

def city_selection_keyboard():
    """Клавиатура выбора города"""
    city_selection_key = InlineKeyboardMarkup()
    moscow_button = InlineKeyboardButton(text='Москва', callback_data='moscow_button')
    nizhniy_novgorod_button = InlineKeyboardButton(text='Нижний Новгород', callback_data='nizhniy_novgorod_button')
    city_selection_key.row(moscow_button)
    city_selection_key.row(nizhniy_novgorod_button)

    return city_selection_key

if __name__ == '__main__':
    greeting_keyboards()
    city_selection_keyboard()
