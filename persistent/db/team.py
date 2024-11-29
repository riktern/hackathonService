from persistent.db.base import Base, WithId
from sqlalchemy import Column, Text, Integer, Boolean, DateTime, Float
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime


# Таблица для команды
class Team(Base, WithId):
    __tablename__ = "team"

    team_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    owner_id = Column(Integer, nullable=False)
    name = Column(Text, nullable=False)
    size = Column(Integer, nullable=False)
    members = Column(ARRAY(Integer), default=[], nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)