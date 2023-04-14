import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('POSTGRES_DB')
USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')

engine = create_engine(
    f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
