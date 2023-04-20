from fastapi import FastAPI, Depends , status, HTTPException, Response
from typing import List
from schima import structure,show_data
from database import Base, engine, SessionLocal
from models import User
from sqlalchemy.orm import Session


def db_get():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

Base.metadata.create_all(bind=engine)



@app.post("/user{id}",status_code=201,response_model=show_data)
def signup(id:int,
           user_name : str, 
           email: str,
           password  :str,          
           address   : str,
           responce : Response,
           request   : structure,
           db :  Session = Depends(db_get)
           ):
    try:
        u = User(user_name=request.user_name, email=request.email ,password = request.password , address = request.address)
        db.add(u)
        db.commit()
        return u
    except Exception as e:
        return e