import pydantic 
from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime 


class UserCreate(BaseModel): #this is the BaseModel of what data is going through our api request. This is validating a user to be created.

  """
  This is a Request Model. This is what users are allowed to post to our api POST/users.

  """
  
  email: EmailStr #Emailstr automatically validates Email addressed data making it sure its not mall intent
  username: str = Field(min_length=8, max_length=25) #Field(min and max length) makes it able to set a min and a max how many characters per field 
  password: str = Field(min_length=8, max_length=25)
  bio: str | None=Field(min_length=5, max_length=100) #having str | None makes it able to where this isnt a manditory requriment for the user to put in 

class UserRead(BaseModel): 
  """
  This is the basemodel for get request. This will define the data of what people are allowed to recieve back. 
  This inherantly provides security for our apis making to where people cant just get data there not allowed to grab. 
  """
  model_config = ConfigDict(
    from_attributes=True)       # when using pydantic to only allows dictionaris pass through but having this here allows attributes as well. This will allow sqlalchemy to work with pydantic instead of just having a Validation error because its not a dict
    
  email:EmailStr
  username: str
  bio: str | None 
  created_at: datetime 
  



