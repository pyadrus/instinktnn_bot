import sqlite3


def creating_a_database_of_tables():
    """
    Создание таблиц: users, users_bonus
    users - запись данных пользователей запистивших бота
    users_bonus - запись данных пользователей получивших бонус
    """
    # Подключение к базе данных SQLite
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    # Создаем таблицу, если она не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, 
                                                        first_name TEXT, last_name TEXT, username TEXT, date TEXT)''')
    # Создание таблицы
    cursor.execute('''CREATE TABLE IF NOT EXISTS users_bonus (user_key TEXT PRIMARY KEY, id INTEGER, full_name TEXT, 
                                                            user_name TEXT, bonus TEXT, plase TEXT, FOREIGN KEY (id) 
                                                            REFERENCES users (id))''')
    conn.commit()  # Сохраняем изменения
    



if __name__ == '__main__':
    creating_a_database_of_tables()