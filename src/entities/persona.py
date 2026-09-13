from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.conection import Base


class Persona(Base):
    __tablename__ = "personas"

    id_persona: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    apellido: Mapped[str] = mapped_column(String(100))
    correo: Mapped[str] = mapped_column(String(100))

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} ({self.correo})"
