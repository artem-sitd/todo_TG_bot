import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    telegram_api_key = os.getenv("telegram_api_key")
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_PORT = os.getenv("DATABASE_PORT")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")
    WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")

    @property
    def webhook_url(self):
        return f'{self.WEBHOOK_HOST}{self.WEBHOOK_PATH}'
