import models.empleados
import schemas.empleados
from sqlalchemy.orm import Session

# crud para los empleados
def create_empleado(db: Session, empleado: schemas.empleados.EmpleadoCreate):
    db_empleado = models.empleados.Empleado(**empleado.dict())
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

def get_empleado_by_nombre(db: Session, nombres: str, apellidos: str):
    return db.query(models.empleados.Empleado).filter(
        models.empleados.Empleado.nombres == nombres ,
        models.empleados.Empleado.apellidos == apellidos).first()


def get_empleado(db: Session, id: int):
    return db.query(models.empleados.Empleado).filter(models.empleados.Empleado.id == id).first()

def update_empleado(db: Session, id: int, empleado: schemas.empleados.EmpleadoUpdate):
    db_empleado = db.query(models.empleados.Empleado).filter(models.empleados.Empleado.id == id).first()
    if db_empleado:
        for key, value in empleado.dict(exclude_unset=True).items():
            setattr(db_empleado, key, value)
        db.commit()
        db.refresh(db_empleado)
        return db_empleado    
    return None

def delete_empleado(db: Session, id: int):
    db_empleado = db.query(models.empleados.Empleado).filter(models.empleados.Empleado.id == id).first()
    if db_empleado:
        db.delete(db_empleado)
        db.commit()
    return db_empleado
  

# crud para las direcciones
def create_direccion(db: Session, direccion: schemas.empleados.DireccionCreate):
    db_direccion = models.empleados.Direccion(**direccion.dict())
    db.add(db_direccion)
    db.commit()
    db.refresh(db_direccion)
    return db_direccion

def get_direccion(db: Session, id: int):
    return db.query(models.empleados.Direccion).filter(models.empleados.Direccion.id_direccion == id).first()

def update_direccion(db: Session, id: int, direccion: schemas.empleados.DireccionUpdate):
    db_empleado = db.query(models.empleados.Direccion).filter(models.empleados.Direccion.id_direccion ==id ).first()
    if db_empleado:
        for key, value in direccion.dict(exclude_unset=True).items():
            setattr(db_empleado, key, value)
        db.commit()
        db.refresh(db_empleado)
        return db_empleado
    return None

def delete_direccion(db: Session, id: int):
    db.query(models.empleados.Direccion).filter(models.empleados.Direccion.id_direccion == id).delete(synchronize_session=False)
    db.commit()
    return id