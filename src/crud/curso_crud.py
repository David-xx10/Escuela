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
            return curso
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

            if (
                curso.id_curso != id_curso
                and session.query(Curso).filter_by(id_curso=curso.id_curso).first()
                is not None
            ):
                raise ValueError("El nuevo ID ya pertenece a otro curso.")

            curso_actual.id_curso = curso.id_curso
            curso_actual.nombre = curso.nombre
            curso_actual.creditos = curso.creditos
            curso_actual.id_facultad = curso.id_facultad
            session.commit()
            return curso_actual
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
        finally:
            session.close()

    def listar_cursos(self) -> list[Curso]:
        session = get_session()
        try:
            return session.query(Curso).all()
        finally:
            session.close()
