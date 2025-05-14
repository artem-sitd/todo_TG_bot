from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Config(BaseSettings):
    telegram_api_key: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_NAME: str
    WEBHOOK_HOST: str
    WEBHOOK_PATH: str
    REDIS_HOST:str
    REDIS_PORT:str

    @property
    def webhook_url(self):
        return f'{self.WEBHOOK_HOST}{self.WEBHOOK_PATH}'


settings = Config()
