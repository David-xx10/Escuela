# from src.entities.persona import Persona


# class Profesor(Persona):
#   def __init__(
#      self, id_persona: int, nombre: str, apellido: str, correo: str, id_profesor: int
# ):
#   super().__init__(id_persona, nombre, apellido, correo)

#  if not isinstance(id_profesor, int) or id_profesor <= 0:
# raise ValueError("El id del profesor debe ser un entero positivo.")
#
# self.id_profesor = id_profesor

# def __str__(self) -> str:
#   return f"{super().__str__()} - Profesor #{self.id_profesor}"
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.database.conection import Base


class Profesor(Base):
    __tablename__ = "profesores"

    id_profesor: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    apellido: Mapped[str] = mapped_column(String(100))
    correo: Mapped[str] = mapped_column(String(100))
