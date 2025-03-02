from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL_DATABASE = 'mysql+mysqlconnector://root:QWERTYqwerty2%40@localhost:3306/Radian_Server'
URL_DATABASE = 'sqlite:///./radian_case_study.db'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()