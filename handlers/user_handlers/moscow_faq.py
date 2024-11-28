from aiogram import types, F

from messages.message_text_faq import moscow_message_text_faq
from system.dispatcher import dp, bot, router

"""FAQ"""

@router.callback_query(F.data == "moscow_reference")
async def moscow_faq_handler(callback_query: types.CallbackQuery):
    """Пояснение для пользователя FAG"""
    # disable_web_page_preview=True - скрыть предпросмотр ссылок в Telegram
    await bot.send_message(callback_query.from_user.id, moscow_message_text_faq, disable_web_page_preview=True,
                           parse_mode=types.ParseMode.HTML)


def moscow_faq_handlers():
    """Регистрируем handlers для калькулятора"""
    dp.register_message_handler(moscow_faq_handler)  # Пояснение для пользователя FAG
