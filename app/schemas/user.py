import datetime
from typing import Optional

from fastapi_users import models


class User(models.BaseUser):
    first_name: str
    birthdate: Optional[datetime.date]


class UserCreate(models.BaseUserCreate):
    first_name: str
    birthdate: Optional[datetime.date]


class UserUpdate(models.BaseUserUpdate):
    first_name: Optional[str]
    birthdate: Optional[datetime.date]


class UserDB(User, models.BaseUserDB):
    pass
