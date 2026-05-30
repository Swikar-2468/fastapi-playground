from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQL_ALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:Q!W%40E%23123@localhost/fastapi'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)

Base = declarative_base()

def get_db(): #get a session to the database for every request
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()