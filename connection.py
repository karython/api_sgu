from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

load_dotenv()

# Configurações do banco de dados
DB_TYPE = os.getenv('DB_TYPE', 'sqlite')  

if DB_TYPE == 'sqlite':
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
else:
    HOST = os.getenv('HOST')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    PORT = os.getenv('PORT')
    DB = os.getenv('DB')
    
    SQLALCHEMY_DATABASE_URI = f"mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

SECRET_KEY = os.getenv('SECRET_KEY')    
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configurações do Flask
SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    connection = engine.connect()
    print(f"Connected to {DB_TYPE} database")
except Exception as e:
    print(f"Failed to connect to database: {e}")
    connection = None