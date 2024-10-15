from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
import config.db
import crud.view
import models.view
import schemas.view
import crud


view = APIRouter()

models.view.Base.metadata.create_all(bind=config.db.engine) 

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@view.get("/empleados/", response_model=List[schemas.view.EmpleadoDireccion], tags=['Empleados-Jerarquia'])
def get_empleados(skip: int = 0, limit: int = 30, db: Session = Depends(get_db)):
    empleados_lista = crud.view.get_empleados(db, skip=skip, limit=limit)
    return empleados_lista        

#Vista de empleados
