from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
db = Session()

Base = declarative_base()


def initialize_db():
    Base.metadata.create_all(bind=engine)
