from fastapi_users_db_sqlalchemy.guid import GUID

from sqlalchemy import Column, Text, ForeignKey, Integer

from app.models.base_model import BaseModel


class Donation(BaseModel):
    __mapper_args__ = {'polymorphic_identity': __name__}
    # user_id = Column(GUID, ForeignKey('user.id'))
    user_id = Column(Integer, default=1)
    comment = Column(Text)
