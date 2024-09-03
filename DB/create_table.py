import psycopg2
from psycopg2 import sql

def create_table():
    # Параметры подключения
    conn = psycopg2.connect(
        dbname="coin_base",
        user="artem",
        password="010203",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # SQL-запрос для создания таблицы
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL
    );
    '''

    # Выполнение запроса
    cur.execute(create_table_query)
    conn.commit()

    # Закрытие соединения
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_table()
