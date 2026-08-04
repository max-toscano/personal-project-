"""
models.py is what the databases will look like, it is the blueprint for the database and how it will be structured.
this is where we will make our orm model to first define what the table we are querying from will look like

"""
from sqlalchemy import CheckConstraint, Datetime, String, Text, func, Integer
from sqlalchemy.orm import  Mapped, mapped_column
from database import Base 

class User(Base): #this is our orm model for the table we are pulling from 

    __tablename__ ="Users"

    __table_args__ = (
        CheckConstraint("length(username) >= 3", name="ck_users_username_len"),  #this signifies some constraitns of the db. CheckConstraints is mapped out like this Check <sql> Constraints <sql> those strings are just sql 

    )

    id: Mapped[int] = mapped_column(Integer(50), primary_key=True) # this is mapped out to be the primary key of the table we are mapping
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True) #index=True make it to where i
    username: Mapped[str] = mapped_column(String(100), index=True) 
    hashed_password: Mapped[str] = mapped_column(String(50))
    bio: Mapped[str | None ] = mapped_column(Text, default=None) #having [str | None] and default=None makes this data optional for the user 
    created_at: Mapped[Datetime] = mapped_column(Datetime(timezone=True), server_default=func.now()) #this is a timestamp for when the user was created and it will automatically set the time to now when the user is created


def __repr__(self) -> str: 
    return f"<User id{self.id} username={self.username!r}>" #this is just for better quality of production. when you print out a user it will give you more information when using this function 