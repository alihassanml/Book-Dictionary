from fastapi import FastAPI,Form,Depends,HTTPException
from typing import Optional
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel,Field
from database import engine,sessionlocal



app = FastAPI()


model.Base.metadata.create_all(bind=engine)

# -------------------------------------------

class Todo(BaseModel):
    title : str 
    description : Optional[str]
    rating : int = Field(gt=0,lt=5)

# -------------------------------------------




def Get_db():
    try:
        db = sessionlocal()
        yield db
    finally:
        db.close()

# -------------------------------------------

def Error():
    raise HTTPException(status_code=404,detail='')


# -------------------------------------------

            # Read Datbase

# -------------------------------------------

@app.get('/')
async def Read_all(db : Session = Depends(Get_db)):
    data = db.query(model.User).all()
    if data is None:
        raise HTTPException(status_code=404,detail='Database is empty')
    return data

# -------------------------------------------

            # Creata Datbase

# -------------------------------------------


@app.post('/')
async def Create(Data : Todo, db:Session=Depends(Get_db)):
    model_user = model.User()
    model_user.title = Data.title
    model_user.description = Data.description
    model_user.rating = Data.rating
    db.add(model_user)
    db.commit()
    raise HTTPException(status_code=200,detail='Successful Added')




# -------------------------------------------

            # Update Database

# -------------------------------------------


@app.put('/{todo.id}')
async def update(todo_id:int,todo:Todo,db : Session = Depends(Get_db)):
    data = db.query(model.User).filter(model.User.id == todo_id).first()
    data.title = todo.title
    data.description = todo.description
    data.rating = todo.rating
    db.add(data)
    db.commit()
    return {'Data':'Successfull update'}





# -------------------------------------------

            # Search Database

# -------------------------------------------




@app.get('/{todo.id}')
async def Search(todo_id:int,db : Session = Depends(Get_db)):
    data = db.query(model.User).filter(model.User.id == todo_id).first()
    return {'Data':data}



# -------------------------------------------

            # Delete Database

# -------------------------------------------



@app.delete('/')
async def Delete(todo_id:int,db : Session = Depends(Get_db)):
    data = db.query(model.User).filter(model.User.id == todo_id).first()
    if data is None:
        raise HTTPException(status_code=200,detail='Data Not Found')
    db.query(model.User).filter(model.User.id == todo_id).delete()
    db.commit()
    raise HTTPException(status_code=200,detail=f'ID : {todo_id} Successful delete')
    



