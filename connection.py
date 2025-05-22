from dotenv import load_dotenv
import os

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey

load_dotenv()

HOST = os.getenv('HOST')

USER= os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
PORT = os.getenv('PORT')
DB = os.getenv('DB')
print(HOST)
print(PASSWORD)

SECRET_KEY = os.getenv('SECRET_KEY')    

SQLALCHEMY_DATABASE_URI = f"mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    connection = engine.connect()
    print("Connected to database")
except Exception as e:
    print(f"Failed to connect to database: {e}")
    connection = None