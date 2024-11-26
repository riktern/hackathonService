# Указываем базовый образ Python
FROM python:3.10-alpine3.20

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей (если у вас есть requirements.txt)
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем оставшиеся файлы проекта
COPY . .

# Указываем порт, который будет слушать приложение
EXPOSE 8000

# Указываем команду запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
