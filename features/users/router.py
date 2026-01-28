"""
Módulo de rutas (Router) para la gestión de usuarios.
Contiene las operaciones CRUD (Create, Read, Update, Delete).
"""
from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException, status

# Ajusta este import según tu estructura de carpetas real
from common.database.models.db_model import User, Gender, Role

# Creamos una instancia del router para agrupar los endpoints
user_router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)


# --- Base de Datos Simulada (Diccionario de Datos en Memoria) ---
# Usamos una lista para simular la tabla de usuarios
fake_db: List[User] = [
    User(
        name="Marcos",
        age=25,
        lastname="Dev",
        gender=Gender.MALE,
        roles=[Role.ADMIN]
    )
]


@user_router.get("/", response_model=List[User])
async def get_all_users():
    """
    Retorna la lista completa de usuarios registrados.
    """
    return fake_db


@user_router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    """
    Crea un nuevo usuario y lo añade a la base de datos.
    """
    # Simulamos la inserción
    fake_db.append(user)
    return user


@user_router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: UUID):
    """
    Busca y retorna un usuario específico por su ID.
    """
    for user in fake_db:
        if user.id == user_id:
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )


@user_router.put("/{user_id}", response_model=User)
async def update_user(user_id: UUID, user_update: User):
    """
    Actualiza los datos de un usuario existente.
    """
    for index, user in enumerate(fake_db):
        if user.id == user_id:
            # Actualizamos manteniendo el ID original para consistencia
            updated_user = user_update.model_copy(update={"id": user_id})
            fake_db[index] = updated_user
            return updated_user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado para actualizar"
    )


@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: UUID):
    """
    Elimina un usuario de la base de datos por su ID.
    """
    for index, user in enumerate(fake_db):
        if user.id == user_id:
            fake_db.pop(index)
            return  # 204 No Content no retorna cuerpo

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado para eliminar"
    )
    