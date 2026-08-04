from fastapi import FastAPI, Depends, HTTPException, Path, Status 
from sqlalchemy import create_engine, string, Integer, Column 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker

engine=create_engine("sqlite.db:///.app.db")

class Base(DeclarativeBase): 
    pass 

class User(Base): 
    __tablename__="Users"

    id:Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[str] =mapped_column(string(225), unique=True)
    username:Mapped[str] = mapped_column(string(225))


SessionLocal=sessionmaker(bind=engine)
db=SessionLocal




app = FastAPI()


@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

 #   The function will return a JSON response with the user_id.