import configparser

from aiogram import Bot
from aiogram import Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage

config = configparser.ConfigParser(empty_lines_in_values=False, allow_no_value=True)
config.read("setting/config.ini")
bot_token = config.get('BOT_TOKEN', 'BOT_TOKEN')

bot = Bot(token=bot_token)

storage = MemoryStorage()  # Хранилище
dp = Dispatcher(storage=storage)

router = Router()
dp.include_router(router)
