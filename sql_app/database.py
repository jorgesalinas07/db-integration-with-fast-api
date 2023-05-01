from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import os
from os.path import dirname, join

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

db_username = os.environ.get("DB_USERNAME", "user_test")
db_pass = os.environ.get("DB_PASS", "postgres")
db_name = os.environ.get("DB_NAME", "test_db")
db_port = os.environ.get("DB_PORT", "1234")
db_host = os.environ.get("DB_HOST", "localhost")

db_string = "postgresql://"+db_username+":"+db_pass+"@"+db_host+":"+db_port+"/"+db_name
engine = create_engine(
    db_string
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
