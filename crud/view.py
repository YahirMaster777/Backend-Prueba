import models.view
from sqlalchemy.orm import Session

import models.view
#obtener empleados del view
def get_empleados(db: Session, skip: int = 0, limit: int = 30):
    return db.query(models.view.EmpleadoDireccion).offset(skip).limit(limit).all()

