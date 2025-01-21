from sqlalchemy import Column, Integer, String
from app.database import TABLE, Base

class Cliente(Base):
    __tablename__ = TABLE
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
