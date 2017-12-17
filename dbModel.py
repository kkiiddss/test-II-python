from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
DB_connect = 'postgres://woruvugwifnphc:d7d6da2c241d65e87abd324ecfa077057bd42a8a919a79fc80b53fbb6e657aab@ec2-184-72-228-128.compute-1.amazonaws.com:5432/del6ucpoe5ftf2e'


class Images(Base):
    __tablename__ = 'Images'

    id = Column(Integer, primary_key=True)
    Url = Column(String)
    CreateDate = Column(DateTime(timezone=True), server_default=func.now())


if __name__ == '__main__':
    engine = create_engine(DB_connect)
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
