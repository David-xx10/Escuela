from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.database.conection import Base


class Profesor(Base):
    __tablename__ = "profesores"

    id_profesor: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    apellido: Mapped[str] = mapped_column(String(100))
    correo: Mapped[str] = mapped_column(String(100))
