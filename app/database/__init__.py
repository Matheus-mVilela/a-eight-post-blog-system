from environs import Env
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

env = Env()
env.read_env()
DB_URL = env('DB_URL')
engine = create_engine(DB_URL)
Base = declarative_base()

_Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = _Session()
