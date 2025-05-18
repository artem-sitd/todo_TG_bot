from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Config(BaseSettings):
    telegram_api_key: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    POSTGRES_DB: str
    WEBHOOK_HOST: str
    WEBHOOK_PATH: str
    REDIS_HOST: str
    REDIS_PORT: int
    DJANGO_HOST: str
    DJANGO_PORT: int
    AIOHTTP_HOST: str
    AIOHTTP_PORT: int

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parent / ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @property
    def webhook_url(self):
        return f'{self.WEBHOOK_HOST}{self.WEBHOOK_PATH}'

    @property
    def django_url(self):
        return f'http://{self.DJANGO_HOST}:{self.DJANGO_PORT}/'

    @property
    def aiohttp_url(self):
        return f'http://{self.AIOHTTP_HOST}:{self.AIOHTTP_PORT}/'


settings = Config()
