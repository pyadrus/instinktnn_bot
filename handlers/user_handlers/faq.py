from aiogram import types, F

from messages.message_text_faq import message_text_faq
from system.dispatcher import dp, bot, router

"""FAQ"""


@router.callback_query(F.data == "reference")
async def faq_handler(callback_query: types.CallbackQuery):
    """Пояснение для пользователя FAG"""
    # disable_web_page_preview=True - скрыть предпросмотр ссылок в Telegram
    await bot.send_message(callback_query.from_user.id, message_text_faq, disable_web_page_preview=True,
                           parse_mode=types.ParseMode.HTML)


def faq_handlers():
    """Регистрируем handlers для калькулятора"""
    dp.register_message_handler(faq_handler)  # Пояснение для пользователя FAG
