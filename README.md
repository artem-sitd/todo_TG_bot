# ✅ Telegram ToDo Bot

Telegram-бот для управления задачами с напоминаниями. Пользователи могут создавать задачи с тегами и датами уведомлений. Бот отправляет напоминания в указанное время, используя Celery и PostgreSQL. Развёртывание осуществляется с помощью Docker Compose.

---

## 🚀 Возможности

- 📝 Создание задач с тегами и датами уведомлений
- ⏰ Отправка напоминаний в указанное время
- 🗂️ Хранение задач в PostgreSQL
- 🐍 Асинхронная обработка задач с использованием Celery
- 🐳 Развёртывание с использованием Docker Compose

---

## 🧰 Технологии

- Python 3.10+
- aiogram
- PostgreSQL
- Celery
- Redis
- Docker & Docker Compose

---

## ⚙️ Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/artem-sitd/todo_TG_bot.git
   cd todo_TG_bot
   ```

2. **Настройте переменные окружения:**

   Переименуйте файл `.env.template` в `.env`:

   ```bash
   cp .env.template .env
   ```

   Отредактируйте файл `.env`, указав необходимые значения:

   - `TELEGRAM_API_KEY` — токен вашего бота, полученный у [@BotFather](https://t.me/BotFather)
   - `WEBHOOK_HOST` — публичный HTTPS-домен для вебхуков (например, с использованием [localtunnel](https://theboroer.github.io/localtunnel-www/))

3. **Установите localtunnel (для локального тестирования):**

   ```bash
   npm install -g localtunnel
   lt --port 8082
   ```

   Скопируйте предоставленный URL и вставьте его в переменную `WEBHOOK_HOST` в файле `.env`.

4. **Запустите приложение с помощью Docker Compose:**

   ```bash
   docker-compose up --build
   ```

---

## 📁 Структура проекта

```
├── aio_bot/               # Логика Telegram-бота
├── app/                   # Основная логика приложения
├── etc/                   # Конфигурационные файлы и Dockerfile
├── .env.template          # Шаблон переменных окружения
├── docker-compose.yml     # Конфигурация Docker Compose
├── requirements.txt       # Зависимости проекта
└── README.md              # Документация проекта
```

---

## 📄 Лицензия

Проект распространяется под лицензией MIT. Подробнее см. файл `LICENSE`.
