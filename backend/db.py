import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DB_NAME = os.getenv('DB_NAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

engine = create_engine(
    f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
