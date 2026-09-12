from src.database.conection import get_session
from src.entities.facultad import Facultad


class FacultadCRUD:
    def __init__(self):
        pass

    def crear_facultad(self, facultad: Facultad) -> Facultad:
        session = get_session()
        try:
            if (
                session.query(Facultad)
                .filter_by(id_facultad=facultad.id_facultad)
                .first()
                is not None
            ):
                raise ValueError("Ya existe una facultad con ese ID.")

            session.add(facultad)
            session.commit()
            return facultad
        finally:
            session.close()

    def obtener_facultad(self, id_facultad: int) -> Facultad | None:
        session = get_session()
        try:
            return session.query(Facultad).filter_by(id_facultad=id_facultad).first()
        finally:
            session.close()

    def actualizar_facultad(
        self, id_facultad: int, facultad: Facultad
    ) -> Facultad | None:
        session = get_session()
        try:
            facultad_actual = (
                session.query(Facultad).filter_by(id_facultad=id_facultad).first()
            )
            if facultad_actual is None:
                return None

            if (
                facultad.id_facultad != id_facultad
                and session.query(Facultad)
                .filter_by(id_facultad=facultad.id_facultad)
                .first()
                is not None
            ):
                raise ValueError("El nuevo ID ya pertenece a otra facultad.")

            facultad_actual.id_facultad = facultad.id_facultad
            facultad_actual.nombre = facultad.nombre
            session.commit()
            return facultad_actual
        finally:
            session.close()

    def eliminar_facultad(self, id_facultad: int) -> bool:
        session = get_session()
        try:
            facultad = (
                session.query(Facultad).filter_by(id_facultad=id_facultad).first()
            )
            if facultad is None:
                return False

            session.delete(facultad)
            session.commit()
            return True
        finally:
            session.close()

    def listar_facultades(self) -> list[Facultad]:
        session = get_session()
        try:
            return session.query(Facultad).all()
        finally:
            session.close()
