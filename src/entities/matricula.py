from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.conection import Base


class Matricula(Base):
    __tablename__ = "matriculas"

    id_matricula: Mapped[int] = mapped_column(primary_key=True)
    id_estudiante: Mapped[int] = mapped_column()
    id_curso: Mapped[Optional[int]] = mapped_column(
        ForeignKey("cursos.id_curso"), nullable=True
    )
    id_grupo: Mapped[Optional[int]] = mapped_column(
        ForeignKey("grupos.id_grupo"), nullable=True
    )
    fecha_matricula: Mapped[str] = mapped_column(String(20))