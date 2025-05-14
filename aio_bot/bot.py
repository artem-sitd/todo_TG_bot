from aiogram.enums import ParseMode
from aiogram import Bot
from aiogram.client.bot import DefaultBotProperties
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import settings
from .routes import router

bot = Bot(token=settings.telegram_api_key, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)
