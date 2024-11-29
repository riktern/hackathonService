from persistent.db.base import Base, WithId
from sqlalchemy import Column, Text, Integer, Boolean, DateTime, Float
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime

# Таблица ролей для хакатонов
class Role(Base, WithId):
    __tablename__ = "role"

    role_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
