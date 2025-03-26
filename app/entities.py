from sqlalchemy import Column, Integer, String
from .database import Base


class Word(Base):
    __tablename__ = "words"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    definition = Column(String, nullable=True)