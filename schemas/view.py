
from pydantic import BaseModel

class EmpleadoDireccion(BaseModel):
    NombreJefe: str
    Direccion: str
    NombreEmpleado: str
    DireccionEmpleado: str
    
    class Config:
        orm_mode = True    