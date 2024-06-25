from sqlalchemy import Boolean,Column,Integer,String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    description = Column(String)
    rating = Column(Integer)