
from typing import Optional
from pydantic import BaseModel

class EmpleadoBase(BaseModel):
    nombres: str
    apellidos: str
    curp:str
    puesto :Optional[str]
    clave_jefe: Optional[int]
    calle: str
    numero_exterior: int
    numero_interior: Optional[int]
    colonia: str
    municipio: str
    estado: str
    pais: str



class EmpleadoCreate(EmpleadoBase):
    nombres: str
    apellidos: str
    curp:str
    puesto :Optional[str] = None
    clave_jefe: Optional[int] = None
    calle: str
    numero_exterior: int
    numero_interior: Optional[int] = None
    colonia: str
    municipio: str
    estado: str
    pais: str

class EmpleadoUpdate(EmpleadoBase):
    nombres: str
    apellidos: str
    curp:str
    puesto :Optional[str]
    clave_jefe: Optional[int]
    calle: str
    numero_exterior: int
    numero_interior: Optional[int]
    colonia: str
    municipio: str
    estado: str
    pais: str


class Empleado(EmpleadoBase):
    id: int
    class Config:
        orm_mode = True
        
    
        