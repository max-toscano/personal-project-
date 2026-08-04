import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine 
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, Session 


load_dotenv #this loads in the hidden .env file 

DATABASE_URL = os.getenv("DATABASE_URL") # this gets your database url from your hidden .env file 

engine=create_engine(
    DATABASE_URL, 

    connect_args= {"check_same_thread": False}, #this is used to allow sqlite to have multiple threads at once becuase fastapi runs on a group of different threads so it would crash a lot 

    echo=True #this will automatically set terminal loggins for sql code outputted 
)

SessionLocal= sessionmaker ( 

    bind=engine,  # binds each session to the database url 

    autoflush=False, #when there is pending work to the database, it will not automatically flush it to the database, you will have to do it manually

    expire_on_commit=False, # so when expire_on_commit is set to True it puts every query into a state where it is expired and will have to be reloaded from the database, this is not good for performance so we set it to false
)

class Base(DeclarativeBase): 
    pass 

def get_db():
    db: Session = SessionLocal()
    try:
        yield db 
    finally: 
            db.close()
