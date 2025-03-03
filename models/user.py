from sqlalchemy import Boolean, Column, Integer, String, Date
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    first_name = Column(String(50))
    middle_initial = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50), unique=True)
    date_of_birth = Column(Date)
    address = Column(String(50))
    tier = Column(String(50))
    billing_period = Column(String(50))