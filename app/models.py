"SQLAlchemy database models"
import uuid

from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TestInt(Base):
    __tablename__ = "testint"

    id = Column(Integer, primary_key=True, unique=True)

class TestUUID(Base):
    __tablename__ = "testuuid"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
