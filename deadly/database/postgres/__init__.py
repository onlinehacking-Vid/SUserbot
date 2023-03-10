import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session





if hasattr(sys, "getandroidapilevel"):
    database = "sqlite:///deadly.db"
else:
    from config import Config
    database = Config.DB_URI

if not database:
    database = "sqlite:///deadly.db"


def start() -> scoped_session:
    engine = create_engine(database)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start() 
