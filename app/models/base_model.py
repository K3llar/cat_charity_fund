import datetime as dt

from sqlalchemy import Column, Boolean, DateTime, Integer

from app.core.db import Base


class BaseModel(Base):
    __abstract__ = True
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=dt.datetime.now)
    close_date = Column(DateTime, default=None, nullable=True)
    __mapper_args__ = {'polymorphic_on': __name__}
