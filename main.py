from aiogram import executor

from handlers.faq import faq_handlers
from handlers.greeting import greeting_handler
from system.dispatcher import dp


def main():
    executor.start_polling(dp, skip_updates=True)
    greeting_handler()
    faq_handlers()


if __name__ == '__main__':
    try:
        main()  # Запуск бота
    except Exception as e:
        print(e)
