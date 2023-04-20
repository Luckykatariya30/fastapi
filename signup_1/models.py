from sqlalchemy import Column, Integer, String,Boolean

from database import Base


class User(Base):
    __tablename__ = "Students"
    studentID = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(23), unique=True, index=True)
    email = Column(String(22), unique=True, index=True)
    password = Column(String(22))
    address = Column(String(33))
   
