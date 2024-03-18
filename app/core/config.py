# app/core/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = 'postgres+asyncpg://postgres:postgres@127.0.0.1:5432/postgresdb'
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()