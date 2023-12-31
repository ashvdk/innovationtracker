from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:123456@localhost/salesdata'


engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()