from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.conection import Base


class Grupo(Base):
    __tablename__ = "grupos"

    id_grupo: Mapped[int] = mapped_column(primary_key=True)
    id_curso: Mapped[int] = mapped_column(ForeignKey("cursos.id_curso"))
    id_profesor: Mapped[int] = mapped_column(ForeignKey("profesores.id_profesor"))
    id_periodo: Mapped[int] = mapped_column(
        ForeignKey("periodos_academicos.id_periodo")
    )
    cupo: Mapped[int] = mapped_column()
