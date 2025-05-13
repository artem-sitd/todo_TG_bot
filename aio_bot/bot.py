from aiogram.enums import ParseMode
from aiogram import Bot
from aiogram.client.bot import DefaultBotProperties
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import Config
from routes import router

bot = Bot(token=Config.telegram_api_key, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)
