from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def greeting_keyboards():
    """Клавиатуры поста приветствия 🎲"""
    keyboards_greeting = InlineKeyboardMarkup()
    get_a_bonus = InlineKeyboardButton(text='Получить бонус', callback_data='get_a_bonus')
    reference_keyboard = InlineKeyboardButton(text='📇 Справка', callback_data='reference')  # Контакты
    keyboards_greeting.row(reference_keyboard, get_a_bonus)
    return keyboards_greeting


if __name__ == '__main__':
    greeting_keyboards()
