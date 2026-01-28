"""
Módulo que define los modelos de datos y enumeraciones para la base de datos.
"""
from typing import List
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, Field

class Gender(str, Enum):
    """Enumeración para los géneros disponibles."""
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class Role(str, Enum):
    """Enumeración para los roles de usuario."""
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class User(BaseModel):
    """
    Modelo de datos que representa a un usuario en el sistema.
    Hereda de Pydantic BaseModel para validación de datos.
    """
    id: UUID = Field(default_factory=uuid4, description="Identificador único del usuario")
    name: str = Field(..., min_length=1, max_length=50, description="Nombre del usuario")
    age: int = Field(..., gt=0, lt=120, description="Edad del usuario")
    lastname: str = Field(..., min_length=1, max_length=50, description="Apellidos")
    gender: Gender = Field(..., description="Género del usuario")
    roles: List[Role] = Field(default=[], description="Lista de roles asignados")
