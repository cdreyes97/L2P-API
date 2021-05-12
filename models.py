from sqlalchemy import Column, String, Integer
from database import Base

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))