from aiogram import executor

from handlers.admin_handlers.admin_handlers import register_admin_handler
from handlers.user_handlers.Dobrolyudova_handlers import register_dobrolyudova_handler
from handlers.user_handlers.Llyicha_handlers import register_ilyich_handler
from handlers.user_handlers.faq import faq_handlers
from handlers.greeting import greeting_handler
from handlers.user_handlers.moscow_faq import moscow_faq_handlers
from system.dispatcher import dp


def main():
    executor.start_polling(dp, skip_updates=True)
    greeting_handler()
    faq_handlers()
    register_admin_handler()
    moscow_faq_handlers()  # Регистрируем handlers для FAQ в Москве
    register_dobrolyudova_handler()  # Регистрируем handlers для Dobrolyudova
    register_ilyich_handler()  # Регистрируем handlers для Ilyich


if __name__ == '__main__':
    try:
        main()  # Запуск бота
    except Exception as e:
        print(e)
