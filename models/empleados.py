from sqlalchemy import Column, Integer, String, ForeignKey
from config.db import Base


class Empleado(Base):
    __tablename__ = 'tbb_empleados'
    
    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(55), nullable=False)
    apellidos = Column(String(100), nullable=False)
    curp = Column(String(55), nullable=False)
    puesto = Column(String(55), nullable=True)
    clave_jefe = Column(Integer, ForeignKey("tbb_empleados.id"), nullable=True)
    #id_direccion = Column(Integer, ForeignKey("tbb_direcciones.id_direccion"))
    
    
class Direccion(Base):
    __tablename__ = 'tbb_direcciones' 
    
    id_direccion = Column(Integer, ForeignKey("tbb_empleados.id"), primary_key=True, nullable=False)
    calle = Column(String(55), nullable=False)
    numero_exterior = Column(Integer, nullable=False)
    numero_interior = Column(Integer, nullable=True)
    colonia= Column(String(55), nullable=False)
    municipio = Column(String(55), nullable=False)
    estado = Column(String(55), nullable=False)
    pais = Column(String(55), nullable=False)        
    

