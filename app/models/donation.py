from fastapi_users_db_sqlalchemy.guid import GUID

from sqlalchemy import Column, Text, ForeignKey

from app.models.base_model import BaseModel


class Donation(BaseModel):
    __mapper_args__ = {'polymorphic_identity': __name__}
    user_id = Column(GUID, ForeignKey('user.id'))
    comment = Column(Text)
