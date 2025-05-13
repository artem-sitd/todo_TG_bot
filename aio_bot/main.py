from aiogram import types
from config import Config
from aiohttp import web
from aio_bot.bot import dp, bot
import asyncio


# прием вебхуков
async def handle_webhook(request):
    print('message from webhook')
    update = await request.json()
    await dp.feed_update(bot, types.Update(**update))
    return web.Response()


# проверка
async def index_page(request):
    return web.Response(
        text='<h1>This is test page. Hello!</h1>',
        content_type='text/html')


async def main():
    try:
        print('start web application aiohttp')
        # Запускаем веб-сервер для приема вебхуков
        app = web.Application()

        # ручка для приема вебхук от телеграма
        app.router.add_post(Config.WEBHOOK_PATH, handle_webhook)

        # просто заглушка
        app.router.add_get('/', index_page)

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, "0.0.0.0", 8080)
        await site.start()

        # Устанавливаем вебхук
        print("set webhooks")
        await bot.set_webhook(Config.webhook_url)

        # Бесконечный цикл для поддержания работы сервера
        await asyncio.Event().wait()
    except asyncio.CancelledError:
        # Обработка остановки сервера
        pass
    finally:
        # Корректное завершение работы
        print('close session, storage, runner')
        await bot.session.close()  # Закрываем сессию бота
        await dp.storage.close()  # Закрываем хранилище диспетчера
        await runner.cleanup()  # Останавливаем веб-сервер


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Сервер остановлен.")
