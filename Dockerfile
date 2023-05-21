# Базовый образ
FROM python:3.9

# Установка переменной среды PYTHONUNBUFFERED в значение "1"
ENV PYTHONUNBUFFERED 1

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование файла requirements.txt в контейнер
COPY requirements.txt /app/

# Установка зависимостей из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остальных файлов проекта в контейнер
COPY . /app/

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
