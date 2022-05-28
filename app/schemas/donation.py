import datetime as dt

from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


class DonationBase(BaseModel):
    # user_id: Optional[int]
    comment: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[PositiveInt]


class DonationCreate(DonationBase):
    full_amount: PositiveInt


class DonationDB(DonationBase):
    id: int
    user_id: Optional[int]
    invested_amount: Optional[int]
    create_date: Optional[dt.datetime]
    close_date: Optional[dt.datetime]
    fully_invested: Optional[bool]

    class Config:
        orm_mode = True
