"""
Punto de entrada principal para la API de Seguridad.
Configura la aplicación FastAPI e incluye los routers.
"""
from fastapi import FastAPI
from features.users.router import user_router

# Inicialización de la aplicación
app = FastAPI(
    title="API Seguridad",
    description="API para gestión de usuarios con arquitectura limpia.",
    version="1.0.0"
)


# Incluir el router de usuarios
app.include_router(user_router)


@app.get("/")
async def root():
    """
    Endpoint raíz para verificar el estado del servicio.
    """
    return {"message": "Hallo desde la API de Seguridad!"}
