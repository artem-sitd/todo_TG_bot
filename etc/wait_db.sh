#!/bin/sh
echo "⏳ Ждём PostgreSQL..."
until nc -z db 5432; do
  sleep 2
done

echo "✅ БД доступна. Применяем миграции..."
python3 app/manage.py makemigrations
python3 app/manage.py migrate

echo "🚀 Запускаем Django..."
exec "$@"
