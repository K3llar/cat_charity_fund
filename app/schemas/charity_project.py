import datetime as dt

from typing import Optional

from pydantic import BaseModel, Field, PositiveInt, root_validator, validator


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[PositiveInt]


class CharityProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):
    pass

    # @root_validator(skip_on_failure=True)
    # def check_fields(cls, values):
    #     for value in values:
    #         if values[value] is None:
    #             raise ValueError(f'Поле {value} не может быть пустым')
    #     return values

    # @validator('name')
    # def name_cant_be_null(cls, value: str):
    #     if value is None:
    #         raise ValueError('Имя не может быть пустым!')
    #     return value


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: Optional[int]
    create_date: Optional[dt.datetime]
    close_date: Optional[dt.datetime]

    class Config:
        orm_mode = True
