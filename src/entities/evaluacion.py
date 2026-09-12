from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.conection import Base


class Evaluacion(Base):
    __tablename__ = "evaluaciones"

    id_evaluacion: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    descripcion: Mapped[str] = mapped_column(String(255))
    tipo: Mapped[str] = mapped_column(String(50))
    id_grupo: Mapped[int] = mapped_column(ForeignKey("grupos.id_grupo"))
    fecha: Mapped[str] = mapped_column(String(20))
    valor_maximo: Mapped[float] = mapped_column()