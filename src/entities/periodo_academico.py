from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.database.conection import Base


class PeriodoAcademico(Base):
    __tablename__ = "periodos_academicos"

    id_periodo: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    fecha_inicio: Mapped[str] = mapped_column(String(10), nullable=False)
    fecha_fin: Mapped[str] = mapped_column(String(10), nullable=False)
    estado: Mapped[str] = mapped_column(String(20), nullable=False, default="activo")
