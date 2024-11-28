import asyncio
import logging
import sys

from loguru import logger

from handlers.admin_handlers.admin_handlers import register_admin_handler
from handlers.greeting import greeting_handler
from handlers.user_handlers.dobrolyudova_handlers import register_dobrolyudova_handler
from handlers.user_handlers.faq import faq_handlers
from handlers.user_handlers.llyicha_handlers import register_ilyich_handler
from handlers.user_handlers.moscow_faq import moscow_faq_handlers
from system.dispatcher import bot
from system.dispatcher import dp

logger.add("logs/log.log", retention="1 days", enqueue=True)  # Логирование бота


async def main():
    try:
        await dp.start_polling(bot)

        greeting_handler()
        faq_handlers()
        register_admin_handler()
        moscow_faq_handlers()  # Регистрируем handlers для FAQ в Москве
        register_dobrolyudova_handler()  # Регистрируем handlers для Dobrolyudova
        register_ilyich_handler()  # Регистрируем handlers для Ilyich

    except Exception as e:
        logger.error(f"Ошибка: {e}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
