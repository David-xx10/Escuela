from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column
from src.database.conection import Base


class Nota(Base):
    __tablename__ = "notas"

    id_nota: Mapped[int] = mapped_column(primary_key=True)
    id_estudiante: Mapped[int]
    id_evaluacion: Mapped[int]
    valor: Mapped[float] = mapped_column(Float)