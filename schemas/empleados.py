
from pydantic import BaseModel

class EmpleadoBase(BaseModel):
    nombres: str
    apellidos: str
    curp:str
    puesto :str 

    
class EmpleadoCreate(EmpleadoBase):
    nombres: str
    apellidos: str
    curp:str
    puesto :str
    clave_jefe: int

class EmpleadoUpdate(EmpleadoBase):
    nombres: str
    apellidos: str
    curp:str
    puesto :str
    id :int

class Empleado(EmpleadoBase):
    id: int
    class Config:
        orm_mode = True
        
        
#---------------------------------------------       

class DireccionBase(BaseModel):
    id_direccion: int
    calle: str
    numero_exterior: int
    colonia: str
    municipio: str
    estado: str
    pais: str
    
class DireccionCreate(DireccionBase):
    pass

class DireccionUpdate(DireccionBase):
    calle: str
    numero_exterior: int
    numero_interior: int
    colonia: str
    municipio: str
    estado: str
    pais: str
    

class Direccion(DireccionBase):
    id_direccion: int
    class Config:
        orm_mode = True