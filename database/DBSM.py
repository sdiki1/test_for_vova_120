from sqlalchemy import create_engine, Column, Integer, String, MetaData, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = 'auth_user'
password = 'wtmybhn17vqphgc'
host = '92.63.179.55'
db_name = 'goldgym'
DATABASE_URL = f"postgresql://{user}:{password}@{host}/{db_name}"

engine = create_engine(DATABASE_URL) 
Base = declarative_base()


class SMS(Base):
    __tablename__ = 'sms'

    Id = Column(Integer, primary_key=True)
    Phone = Column(String)
    Tzid = Column(Integer)
    Sms = Column(Integer)

class Accounts(Base):
    __tablename__ = 'accounts'
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Is_man = Column(Boolean)
    AuthV3 = Column(String)
    Date_active = Column(DateTime)
    Is_using = Column(Boolean)

# class Client(Base):
    # __tablename__ = 'client'



Base.metadata.create_all(engine)

