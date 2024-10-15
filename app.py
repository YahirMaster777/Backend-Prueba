from fastapi import FastAPI
import uvicorn
import os

from routes.view import view
from routes.empleados import empleados
app = FastAPI(
    title="Prueba de Backend",
    description="API para registrar empleados"
)

app.include_router(empleados)
app.include_router(view)