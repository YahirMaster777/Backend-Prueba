from sqlalchemy import Column, Integer, String, ForeignKey
from config.db import Base



class EmpleadoModel(Base):
    __tablename__ = 'tb_empleados'
    
    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(55), nullable=False)
    apellidos = Column(String(100), nullable=False)
    curp = Column(String(55), nullable=False)
    puesto = Column(String(55), nullable=True, default=None) #valor opcional
    clave_jefe = Column(Integer, ForeignKey("tb_empleados.id"), nullable=True, default=None)#valor opcional
    calle = Column(String(55), nullable=False)
    numero_exterior = Column(Integer, nullable=False)
    numero_interior = Column(Integer, nullable=True, default=None)#valor opcional
    colonia= Column(String(55), nullable=False)
    municipio = Column(String(55), nullable=False)
    estado = Column(String(55), nullable=False)
    pais = Column(String(55), nullable=False) 
    

# class EmpleadosSub(Base):
#     __tablename__ = 'tb_organigrama'
    
#     id_jefe= Column(Integer, ForeignKey("tb_empleados.id"))
#     id_subordinado = Column(Integer, ForeignKey("tb_empleados.id")) 