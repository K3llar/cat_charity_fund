from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = ('Приложение Благотворительного фонда '
                      'поддержки котиков.')
    description: str = ('Приложение создано для сбора пожертвований '
                        'на различные целевые проекта поддержки '
                        'наших хвостатых друзей.')
    database_url: str
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
