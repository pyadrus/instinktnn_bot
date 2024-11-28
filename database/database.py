import sqlite3


def creating_a_database_of_tables():
    """
    Создание таблиц: users, users_bonus
    users - запись данных пользователей запустивших бота
    users_bonus - запись данных пользователей получивших бонус
    """

    conn = sqlite3.connect('orders.db')  # Подключение к базе данных SQLite
    cursor = conn.cursor()
    # Создаем таблицу, если она не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, 
                                                        first_name TEXT, last_name TEXT, username TEXT, date TEXT)''')
    # Создание таблицы
    cursor.execute('''CREATE TABLE IF NOT EXISTS users_bonus (user_key TEXT PRIMARY KEY, id INTEGER, full_name TEXT, 
                                                            user_name TEXT, bonus TEXT, plase TEXT, FOREIGN KEY (id) 
                                                            REFERENCES users (id))''')
    conn.commit()  # Сохраняем изменения


def recording_the_data_of_users_who_launched_the_bot(message, current_date):
    """Запись данных пользователей запустивших бота

    Args:
        message: Данные Telegram аккаунта 
        current_date: Время запуска бота
    """

    conn = sqlite3.connect('orders.db')  # Подключение к базе данных SQLite
    cursor = conn.cursor()
    # Записываем данные пользователя в базу данных
    cursor.execute('''INSERT INTO users (user_id, first_name, last_name, username, date) VALUES (?, ?, ?, ?, ?)''', (
        message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username,
        current_date))
    conn.commit()


def get_export_bonus_from_database():
    """Получение данных бонусов из базы данных"""
    conn = sqlite3.connect('orders.db')  # Подключение к базе данных SQLite
    cursor = conn.cursor()
    # Получаем данные всех пользователей из базы данных
    cursor.execute('SELECT * FROM users_bonus')
    data = cursor.fetchall()
    return data


def get_export_user_bonus_from_database():
    """Получение данных бонусов из базы данных"""
    conn = sqlite3.connect('orders.db')  # Подключение к базе данных SQLite
    cursor = conn.cursor()
    # Получаем данные всех пользователей из базы данных
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    return data


def retrieve_user_bonus(user_key):
    conn = sqlite3.connect('orders.db')  # Подключение к базе данных SQLite
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users_bonus WHERE user_key=?", (user_key,))
    existing_user = cursor.fetchone()
    return existing_user


if __name__ == '__main__':
    creating_a_database_of_tables()
