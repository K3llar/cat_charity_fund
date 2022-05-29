from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = ('Приложение Благотворительного фонда '
                      'поддержки котиков.')
    description: str = ('Приложение создано для сбора пожертвований '
                        'на различные целевые проекта поддержки '
                        'наших хвостатых друзей.')
    database_url: str
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = 'env.template'


settings = Settings()
