from sqlalchemy import Column, Integer, String
from config.db import Base

class EmpleadoDireccion(Base):
    __tablename__ = 'view_empleados'
    
    id = Column(Integer, primary_key=True)  
    NombreJefe = Column(String(55))
    Direccion = Column(String(255))
    NombreEmpleado = Column(String(55))
    DireccionEmpleado = Column(String(255))