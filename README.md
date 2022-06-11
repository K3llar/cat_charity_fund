# Фонд помощи животным

Фонд собирает пожертвования на различные целевые проекты такие как: медицинское обслуживание, создание и оснащение приютов и других проектов значимых для жизни животных.


## Технологии

- Python 3.10
- FastAPI
- SQLAlchemy

Примеры запросов к API представлены в файле openapi.json

### Установка проекта

- Скачать проект:

`git clone https://github.com/K3llar/cat_charity_fund.git`

- Выполнить команды:

`cd cat_charity_fund/`

`python -m venv venv`

`source venv/Scripts/activate`

`pip install -r requirements.txt`

- Создать файл .env с настройками проекта

>DATABASE_URL=(например - sqlite+aiosqlite:///./fastapi.db)
>
>SECRET=секретное слово
>
>FIRST_SUPERUSER_EMAIL=
>
>FIRST_SUPERUSER_PASSWORD=

- Применить миграции для создания базы данных

`alembic upgrade head`

- Запустить приложение

`uvicorn app.main:app`
