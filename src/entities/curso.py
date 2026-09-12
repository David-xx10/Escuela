from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.conection import Base


class Curso(Base):
    __tablename__ = "cursos"

    id_curso: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int] = mapped_column()
    id_facultad: Mapped[int] = mapped_column(ForeignKey("facultades.id_facultad"))
