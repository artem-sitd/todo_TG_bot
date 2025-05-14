import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Config(BaseSettings):
    # telegram_api_key = os.getenv("telegram_api_key")
    # DATABASE_USER = os.getenv("DATABASE_USER")
    # DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    # DATABASE_HOST = os.getenv("DATABASE_HOST")
    # DATABASE_PORT = os.getenv("DATABASE_PORT")
    # DATABASE_NAME = os.getenv("DATABASE_NAME")
    # WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
    # WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")
    telegram_api_key: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_NAME: str
    WEBHOOK_HOST: str
    WEBHOOK_PATH: str

    @property
    def webhook_url(self):
        return f'{self.WEBHOOK_HOST}{self.WEBHOOK_PATH}'

settings = Config()