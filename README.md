# Api para el registro de empleados

## AUTOR
Elaborado por: Marvin Yair Tolentino Perez [YahirMaster777](https://github.com/YahirMaster777)

###
Este prueba practica se centra en el desarrollo de un api-rest utilizando Python.
La cual permitirá a los usuarios realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar).


### Tecnologías Utilizadas

[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-FFFFFF?style=for-the-badge&logo=uvicorn&logoColor=black)](https://www.uvicorn.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)

## Pasos para Desplegar el Proyecto

1. **Clonar el repsitorio**

```bash
    git clone https://github.com/YahirMaster777/Backend-Prueba.git
    cd my-project
```

2. **Modificar la url de la base de datos**
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://<user>:<pass>@localhost:3306/prueba_back_db"
```bash
    cd my-project/config/
```

3. **Instalar la dependencias**
    nota: Asegurarse de estar en el directorio raiz del proyecto
```bash
    pip install -r requirements.txt
```
4. **Inicializar el proyecto**
```bash
    -uvicorn uvicorn app:app
```
5 **Visualizar la documentación de la api**
    http://127.0.0.1:8000/docs 
    
