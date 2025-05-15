from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Config(BaseSettings):
    telegram_api_key: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    POSTGRES_DB: str
    WEBHOOK_HOST: str
    WEBHOOK_PATH: str
    REDIS_HOST: str
    REDIS_PORT: str
    DJANGO_HOST: str
    DJANGO_PORT: str
    AIOHTTP_HOST: str
    AIOHTTP_PORT: str

    @property
    def webhook_url(self):
        return f'{self.WEBHOOK_HOST}{self.WEBHOOK_PATH}'

    @property
    def django_url(self):
        return f'http://:{self.DJANGO_HOST}:{self.DJANGO_PORT}/'

    @property
    def aiohttp_url(self):
        return f'http://{self.AIOHTTP_HOST}:{self.AIOHTTP_PORT}/'


settings = Config()
