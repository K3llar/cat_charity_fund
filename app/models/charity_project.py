from sqlalchemy import Column, String, Text

from app.models.base_model import BaseModel


class CharityProject(BaseModel):
    __mapper_args__ = {'polymorphic_identity': 'charityproject'}
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
