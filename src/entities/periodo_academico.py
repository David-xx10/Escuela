from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.database.conection import Base


class PeriodoAcademico(Base):
    __tablename__ = "periodos_academicos"

    id_periodo: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
