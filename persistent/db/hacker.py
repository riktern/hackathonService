from persistent.db.base import Base, WithId

from sqlalchemy import Column, Text, Integer, Boolean, DateTime, Float
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime


class Hacker(Base, WithId):
    __tablename__ = "hacker"

    user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(Text, nullable=False)
    active_teams = Column(ARRAY(Integer), default=[], nullable=False)
    roles = Column(ARRAY(Integer), default=[], nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
