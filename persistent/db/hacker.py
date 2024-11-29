from persistent.db.base import Base, WithId

from sqlalchemy import Column, Text, Integer, Boolean, DateTime, Float
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from datetime import datetime


class Hacker(Base, WithId):
    __tablename__ = "hacker"

    user_uuid = Column(UUID(as_uuid=True), nullable=False, unique=True)
    name = Column(Text, nullable=False)
    active_teams_uuids = Column(ARRAY(UUID(as_uuid=True)), default=[], nullable=False)
    roles_uuids = Column(ARRAY(UUID(as_uuid=True)), default=[], nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
