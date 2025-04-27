FROM postgres:latest

# Настройка переменных окружения
ENV POSTGRES_DB=mydb
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# Опционально: указываем порт (по умолчанию 5432)
EXPOSE 5432

# Опционально: добавляем скрипты инициализации, если они нужны
# COPY ./init.sql /docker-entrypoint-initdb.d/
