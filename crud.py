from sqlalchemy.orm import Session
from . import models,schemas


def get_cliente_by_email(db: Session, email:str):
    return db.query(models.Cliente).filter(models.Cliente.email == email).first()


def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(name=cliente.name,email=cliente.email)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

