from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.conection import Base


class Facultad(Base):
    __tablename__ = "facultades"

    id_facultad: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
