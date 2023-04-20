from pydantic import BaseModel 

class structure(BaseModel):
    user_name: str
    email: str
    password: str
    address:str


class show_data(BaseModel):
    user_name: str
    email: str    
    
    class Config():
        orm_mode = True





