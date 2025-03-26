from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from settings import config

engine = create_engine(config.DB_URL)
Base = declarative_base()

_Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = _Session()
