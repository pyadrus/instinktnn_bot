import datetime  # Дата
import random
import sqlite3  # Импортируем модуль для работы с базой данных SQLite
import time
from datetime import date

from aiogram import types  # Типы пользователя
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from aiogram.dispatcher.filters.state import StatesGroup, State
from loguru import logger

from database.database import recording_the_data_of_users_who_launched_the_bot
from database.database import retrieve_user_bonus
from keyboards.bonus_keyboards import ilyich_keyboards
from messages.bonus_text import random_il
from messages.greeting_post import greeting_post_nizhniy_novgorod
from system.dispatcher import dp, bot  # Подключение к боту и диспетчеру пользователя


class MakingAnOrder(StatesGroup):
    """Создание класса состояний"""
    write_phone = State()


@dp.callback_query_handler(lambda c: c.data == "Ilyich_button")
async def ilyich_button_handler(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()
        await state.reset_state()
        username = callback_query.from_user.username  # Username пользователя бота Telegram
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Получаем текущую дату и время
        logger.info(f'Нажали на кнопку "Ильича" {callback_query.from_user.id, username, current_date}')
        recording_the_data_of_users_who_launched_the_bot(callback_query.message, current_date)
        logger.info(f'Привет! нажали на кнопку /start {callback_query.from_user.id, username, current_date}')
        keyboards_greeting = ilyich_keyboards()
        await bot.send_message(callback_query.from_user.id, text=greeting_post_nizhniy_novgorod,
                               reply_markup=keyboards_greeting,
                               disable_web_page_preview=True,
                               parse_mode=types.ParseMode.HTML)
    except Exception as e:
        logger.error(f'Произошла ошибка: {e}')


@dp.callback_query_handler(lambda c: c.data == "ilyich_kub")
async def share_number(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.send_dice(callback_query.from_user.id, emoji='🎲')  # Отправляем эмодзи '🎲'
    time.sleep(5)
    user_id = callback_query.from_user.id
    today = date.today().strftime('%Y-%m-%d')
    plase = "проспект Ильича, д.25"
    # Проверка, был ли использован бонус сегодня
    user_key = f"{user_id}_{today}"  # Создание уникального ключа

    existing_user = retrieve_user_bonus(user_key)

    if existing_user:
        text_error_bonus = "Вы уже использовали бонус сегодня."
        await bot.answer_callback_query(callback_query.id, text_error_bonus)
        await state.finish()
        return
    text = "✅ Введите ваше имя."
    await bot.send_message(callback_query.from_user.id, text)
    await MakingAnOrder.write_phone.set()
    await state.update_data(user_id=user_id, today=today, plase=plase)


@dp.message_handler(state=MakingAnOrder.write_phone)
async def write_phone(message: types.Message, state: FSMContext):
    """Обработчик ввода номера телефона"""
    data = await state.get_data()
    user_id = data.get('user_id')
    plase = data.get('plase')
    today = data.get('today')
    phone = message.text
    random_bonus = random.choice(random_il)
    user_key = f"{user_id}_{today}"  # Создание уникального ключа
    # Проверяем, существует ли запись с таким же id и user_key в таблице users_bonus
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users_bonus WHERE id=? AND user_key=?", (user_id, user_key))
    existing_user = cursor.fetchone()
    if existing_user:
        text_error_bonus = "Вы уже использовали бонус сегодня."
        await bot.send_message(message.from_user.id, text_error_bonus)
        await state.finish()
        return
    cursor.execute(
        "INSERT INTO users_bonus (user_key, id, full_name, user_name, bonus, plase) VALUES (?, ?, ?, ?, ?, ?)",
        (user_key, user_id, message.from_user.full_name, phone, random_bonus, plase))

    conn.commit()
    await state.finish()
    bonus = (f"🎉 Ура! А вот и твоя награда: {random_bonus}\n\n"

             f"Предъяви эту запись нашему администратору и забирай свой приз 🏆\n\n"

             f"⚠️ ВНИМАНИЕ! Новый бонус можно получить ровно через сутки.\n"
             f"📢 Подписывайся на наш <a href='https://t.me/instinkt_project_nn'>Telegram канал!</a>\n\n"

             f"Для возврата в начало нажми /start.")
    await message.answer(bonus, disable_web_page_preview=True)


def register_ilyich_handler():
    """Регистрируем handlers для Ильича"""
    dp.register_callback_query_handler(ilyich_button_handler)
