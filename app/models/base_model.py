from sqlalchemy import Column, Boolean, DateTime, Integer, String

from app.core.db import Base


class BaseModel(Base):
    __abstract__ = True
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime)
    close_date = Column(DateTime)
    model = Column(String(32), nullable=False)
    __mapper_args__ = {'polymorphic_on': model}

