from os import environ

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    APP_PORT: int = 8000
    POSTGRES_DB: str = 'postgres'
    POSTGRES_USER: str = 'user'
    POSTGRES_PASSWORD: str = 'password'
    POSTGRES_PORT: int = 5432
    DB_URL: str = (
        'postgresql://user:password@host.docker.internal:5432/postgres'
    )
    CHAT_GPT_API_KEY: str = 'very-much-secret'
    
    class Config:
        env_file = environ.get('.env', '.env.example')
        extra = 'allow'


config = Config()
