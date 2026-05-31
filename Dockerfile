FROM python:3.11-slim

# рабочая директория
WORKDIR /app

# зависимости
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# код
COPY . .

# порт FastAPI
EXPOSE 8000

# запуск
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-10000}"]