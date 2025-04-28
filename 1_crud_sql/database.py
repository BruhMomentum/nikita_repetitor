import psycopg2
from psycopg2 import Error
import os

def get_db_connection():
    try:
        # Параметры подключения
        connection = psycopg2.connect(
            host="localhost",  # или IP-адрес контейнера
            port="5432",      # порт, который вы указали при запуске контейнера
            database="mydb",
            user="myuser",
            password="mypassword"
        )

        # Проверка подключения
        print("Успешное подключение к PostgreSQL")
        return connection

    except (Exception, Error) as error:
        print("Ошибка при подключении к PostgreSQL:", error)
        return None

def main():
    # Получаем подключение
    connection = get_db_connection()
    
    if connection:
        try:
            # Создаем курсор для выполнения операций с базой данных
            cursor = connection.cursor()
            
            # Пример выполнения запроса
            cursor.execute("SELECT 5+5;")
            db_version = cursor.fetchone()
            print("Версия PostgreSQL:", db_version)

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL:", error)
        
        finally:
            # Закрываем курсор и соединение
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")

if __name__ == "__main__":
    main()
