from fastapi import APIRouter, Depends, HTTPException
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
        

@empleados.post("/registrar-empleado/", response_model=schemas.empleados.Empleado)
def create_empleado(empleado: schemas.empleados.EmpleadoCreate, db: Session = Depends(get_db)):
    db_empleados = crud.empleados.get_empleado_by_nombre(db, nombres=empleado.nombres, apellidos=empleado.apellidos)
    if db_empleados:
        raise HTTPException(status_code=400, detail="El empleado ya existe")
    
    return crud.empleados.create_empleado(db=db, empleado = empleado)

@empleados.get("/empleado/{id}", response_model=schemas.empleados.Empleado)
def read_empleado(id: int, db: Session = Depends(get_db)):
    db_empleado = crud.empleados.get_empleado(db=db, id=id)
    if db_empleado is None:
        raise HTTPException(status_code=404, detail="El empleado no existe")
    return db_empleado

@empleados.put("/actualizar-empleado/{id}", response_model=schemas.empleados.Empleado)
def update_empleado(id: int, empleado: schemas.empleados.EmpleadoUpdate, db: Session = Depends(get_db)):
    db_empleado = crud.empleados.get_empleado(db, id=id)
    if db_empleado is None:
        raise HTTPException(status_code=404, detail="El empleado no existe")
    return crud.empleados.update_empleado(db, id=id, empleado=empleado)

@empleados.delete("/eliminar-empleado/{id}")
def delete_empleado(id: int, db: Session = Depends(get_db)):
    db_empleado = crud.empleados.get_empleado(db, id=id)
    if db_empleado is None:
        raise HTTPException(status_code=404, detail="El empleado no existe")
    return crud.empleados.delete_empleado(db, id=id)

#Direcciones

@empleados.post("/registrar-direccion/", response_model=schemas.empleados.Direccion)
def create_direccion(direccion: schemas.empleados.DireccionCreate, db: Session = Depends(get_db)):
    return crud.empleados.create_direccion(db, direccion)

@empleados.get("/direccion/{id}", response_model=schemas.empleados.Direccion)
def read_direccion(id: int, db: Session = Depends(get_db)):
    db_direccion = crud.empleados.get_direccion(db=db, id=id )
    if db_direccion is None:
        raise HTTPException(status_code=404, detail="La direccion no existe")
    return db_direccion

@empleados.put("/actualizar-direccion/{id}", response_model=schemas.empleados.Direccion)
def update_direccion(id: int, direccion: schemas.empleados.DireccionUpdate, db: Session = Depends(get_db)):
    db_direccion = crud.empleados.update_direccion(db, id=id, direccion=direccion)
    if db_direccion is None:
        raise HTTPException(status_code=404, detail="La direccion no existe")
    return db_direccion

@empleados.delete("/eliminar-direccion/{id}", response_model=schemas.empleados.Direccion)
def delete_direccion(id: int, db: Session = Depends(get_db)):
    db_direccion = crud.empleados.get_direccion(db=db, id=id)
    if db_direccion is None:
        raise HTTPException(status_code=404, detail="La direccion no existe")
    return db_direccion