from aiogram import executor

from handlers.admin_handlers.admin_handlers import register_admin_handler
from handlers.user_handlers.faq import faq_handlers
from handlers.greeting import greeting_handler
from handlers.user_handlers.moscow_faq import moscow_faq_handlers
from handlers.user_handlers.moscow_handlers import register_moscow_handler
from system.dispatcher import dp


def main():
    executor.start_polling(dp, skip_updates=True)
    greeting_handler()
    faq_handlers()
    register_admin_handler()
    register_moscow_handler()  # Регистрируем handlers для Москвы
    moscow_faq_handlers()  # Регистрируем handlers для FAQ в Москве


if __name__ == '__main__':
    try:
        main()  # Запуск бота
    except Exception as e:
        print(e)