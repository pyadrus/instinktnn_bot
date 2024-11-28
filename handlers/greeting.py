import datetime  # Дата

from aiogram import F
from aiogram import types  # Типы пользователя
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext  # Состояния пользователя
from loguru import logger

from database.database import recording_the_data_of_users_who_launched_the_bot
from keyboards.bonus_keyboards import bonus_keyboards
from keyboards.greeting_keyboards import city_selection_keyboard, greeting_keyboards  # Клавиатуры поста приветствия
from messages.greeting_post import greeting_post_nizhniy_novgorod
from system.dispatcher import dp, bot, router  # Подключение к боту и диспетчеру пользователя

logger.add('log/log.log', rotation='2 MB')


@dp.message(CommandStart())
async def greeting(message: types.Message, state: FSMContext):
    """Обработчик команды /start, он же пост приветствия"""
    await state.clear()

    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Получаем текущую дату и время
    recording_the_data_of_users_who_launched_the_bot(message, current_date)
    logger.info(f'Привет! нажали на кнопку /start {message.from_user.id, message.from_user.username, current_date}')
    city_selection_key = city_selection_keyboard()
    await message.answer('Привет! 👋\n\n 🌟 Я чат-бот сети салонов <i>Инстинкт</i>\n\n 🌟 Лучший релакс в твоем '
                         'городе\n\n', reply_markup=city_selection_key, disable_web_page_preview=True,
                         parse_mode="HTML")


@router.callback_query(F.data == "nizhniy_novgorod_button")
async def moscow_button_handler(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.clear()

        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Получаем текущую дату и время
        logger.info(
            f'Нажали на кнопку "Нижний Новгород" {callback_query.from_user.id, callback_query.from_user.username, current_date}')
        recording_the_data_of_users_who_launched_the_bot(callback_query.message, current_date)
        logger.info(
            f'Привет! нажали на кнопку /start {callback_query.from_user.id, callback_query.from_user.username, current_date}')
        keyboards_greeting = greeting_keyboards()
        await bot.send_message(callback_query.from_user.id, text=greeting_post_nizhniy_novgorod,
                               reply_markup=keyboards_greeting,
                               disable_web_page_preview=True,
                               parse_mode="HTML")
    except Exception as e:
        logger.error(f'Произошла ошибка: {e}')


@router.callback_query(F.data == "get_a_bonus")
async def get_a_bonus(callback_query: types.CallbackQuery):
    bonus_keyboard = bonus_keyboards()
    bonus_posts = 'Выберете филиал:'
    await bot.send_message(callback_query.from_user.id, bonus_posts, reply_markup=bonus_keyboard,
                           parse_mode="HTML")


def greeting_handler():
    """Регистрируем handlers для калькулятора"""
    dp.register_message_handler(greeting)  # Обработчик команды /start, он же пост приветствия
