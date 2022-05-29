from typing import Union

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = ('Приложение Благотворительного фонда '
                      'поддержки котиков.')
    description: str = ('Приложение создано для сбора пожертвований '
                        'на различные целевые проекта поддержки '
                        'наших хвостатых друзей.')
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'iuahgbhiulcb15674dzxcvcnds'
    first_superuser_email: Union[None, EmailStr] = None
    first_superuser_password: Union[None, str] = None

    class Config:
        env_file = '.env'


settings = Settings()
