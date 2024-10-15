import models.empleados
import schemas.empleados
from sqlalchemy.orm import Session

# crud para los empleados
def create_empleado(db: Session, empleado: schemas.empleados.EmpleadoCreate):
    db_empleado = models.empleados.EmpleadoModel(**empleado.dict())
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

def get_empleado_by_nombre(db: Session, nombres: str, apellidos: str):
    return db.query(models.empleados.EmpleadoModel).filter(
        models.empleados.EmpleadoModel.nombres == nombres ,
        models.empleados.EmpleadoModel.apellidos == apellidos).first()


def get_empleado(db: Session, id: int):
    return db.query(models.empleados.EmpleadoModel).filter(models.empleados.EmpleadoModel.id == id).first()

def update_empleado(db: Session, id: int, empleado: schemas.empleados.EmpleadoUpdate):
    db_empleado = db.query(models.empleados.EmpleadoModel).filter(models.empleados.EmpleadoModel.id == id).first()
    if db_empleado:
        for key, value in empleado.dict(exclude_unset=True).items():
            setattr(db_empleado, key, value)
        db.commit()
        db.refresh(db_empleado)
        return db_empleado    
    return None

def delete_empleado(db: Session, id: int):
    db_empleado = db.query(models.empleados.EmpleadoModel).filter(models.empleados.EmpleadoModel.id == id).first()
    if db_empleado:
        db.delete(db_empleado)
        db.commit()
    return db_empleado
