"""
This will create the db we will have to practice on 

"""
from database import Base, engine 
import models 

def main() -> None: 
    print("tables sqlalchemy knows about:", list(Base.metadata.tables.keys()))

    Base.metdata.create_all(bind=engine)
    