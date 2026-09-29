from src.database.conection import get_session
from src.entities.curso import Curso


class CursoCRUD:
    def __init__(self):
        pass

    def crear_curso(self, curso: Curso) -> Curso:
        session = get_session()
        try:
            if (
                session.query(Curso).filter_by(id_curso=curso.id_curso).first()
                is not None
            ):
                raise ValueError("Ya existe un curso con ese ID.")

            session.add(curso)
            session.commit()
            session.refresh(curso)
            return curso
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def obtener_curso(self, id_curso: int) -> Curso | None:
        session = get_session()
        try:
            return session.query(Curso).filter_by(id_curso=id_curso).first()
        finally:
            session.close()

    def actualizar_curso(self, id_curso: int, curso: Curso) -> Curso | None:
        session = get_session()
        try:
            curso_actual = session.query(Curso).filter_by(id_curso=id_curso).first()
            if curso_actual is None:
                return None

            curso_actual.nombre = curso.nombre
            curso_actual.creditos = curso.creditos
            curso_actual.id_facultad = curso.id_facultad
            session.commit()
            session.refresh(curso_actual)
            return curso_actual
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def eliminar_curso(self, id_curso: int) -> bool:
        session = get_session()
        try:
            curso = session.query(Curso).filter_by(id_curso=id_curso).first()
            if curso is None:
                return False

            session.delete(curso)
            session.commit()
            return True
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def listar_cursos(self) -> list[Curso]:
        session = get_session()
        try:
            return session.query(Curso).all()
        finally:
            session.close()
