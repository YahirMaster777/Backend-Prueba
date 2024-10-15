from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
import config.db
import crud.empleados
import models.empleados
import schemas.empleados
import crud


empleados = APIRouter()

models.empleados.Base.metadata.create_all(bind=config.db.engine) 

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@empleados.post("/registrar-empleado/", response_model=schemas.empleados.Empleado , tags=['Empleados'])
def create_empleado(empleado: schemas.empleados.EmpleadoCreate, db: Session = Depends(get_db)):
    db_empleados = crud.empleados.get_empleado_by_nombre(db, nombres=empleado.nombres, apellidos=empleado.apellidos)
    if db_empleados:
        raise HTTPException(status_code=400, detail="El empleado ya existe")
    
    return crud.empleados.create_empleado(db=db, empleado = empleado)

@empleados.get("/empleado/{id}", response_model=schemas.empleados.Empleado, tags=['Empleados'])
def read_empleado(id: int, db: Session = Depends(get_db)):
    db_empleado = crud.empleados.get_empleado(db=db, id=id)
    if db_empleado is None:
        raise HTTPException(status_code=404, detail="El empleado no existe")
    return db_empleado

@empleados.put("/actualizar-empleado/{id}", response_model=schemas.empleados.Empleado, tags=['Empleados'])
def update_empleado(id: int, empleado: schemas.empleados.EmpleadoUpdate, db: Session = Depends(get_db)):
    db_empleado = crud.empleados.get_empleado(db, id=id)
    if db_empleado is None:
        raise HTTPException(status_code=404, detail="El empleado no existe")
    return crud.empleados.update_empleado(db, id=id, empleado=empleado)

@empleados.delete("/eliminar-empleado/{id}" ,tags=['Empleados'])
def delete_empleado(id: int, db: Session = Depends(get_db)):
    db_empleado = crud.empleados.get_empleado(db, id=id)
    if db_empleado is None:
        raise HTTPException(status_code=404, detail="El empleado no existe")
    return crud.empleados.delete_empleado(db, id=id)
