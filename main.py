from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from app import models, schemas,crud
from app.database import engine, Base, get_db


app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hello": "API Working"}

@app.post("/cliente/", response_model=schemas.ClienteResponse)
def create_cliente(cliente:schemas.ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = crud.get_cliente_by_email(db, cliente.email)
    if db_cliente:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_cliente(db, cliente)

@app.get("/cliente/", response_model=list[schemas.ClienteResponse])
def read_clientes(db:Session = Depends(get_db)):
    return db.query(models.Cliente).all()
