from src.database.conection import get_session
from src.entities.matricula import Matricula


class MatriculaCRUD:
    def __init__(self):
        pass

    def crear_matricula(self, matricula: Matricula) -> Matricula:
        session = get_session()
        try:
            if (
                session.query(Matricula)
                .filter_by(id_matricula=matricula.id_matricula)
                .first()
                is not None
            ):
                raise ValueError("Ya existe una matrícula con ese ID.")

            session.add(matricula)
            session.commit()
            return matricula
        finally:
            session.close()

    def obtener_matricula(self, id_matricula: int) -> Matricula | None:
        session = get_session()
        try:
            return (
                session.query(Matricula)
                .filter_by(id_matricula=id_matricula)
                .first()
            )
        finally:
            session.close()

    def actualizar_matricula(
        self, id_matricula: int, matricula: Matricula
    ) -> Matricula | None:
        session = get_session()
        try:
            matricula_actual = (
                session.query(Matricula)
                .filter_by(id_matricula=id_matricula)
                .first()
            )
            if matricula_actual is None:
                return None

            if (
                matricula.id_matricula != id_matricula
                and session.query(Matricula)
                .filter_by(id_matricula=matricula.id_matricula)
                .first()
                is not None
            ):
                raise ValueError("El nuevo ID ya pertenece a otra matrícula.")

            matricula_actual.id_matricula = matricula.id_matricula
            matricula_actual.id_estudiante = matricula.id_estudiante
            matricula_actual.id_curso = matricula.id_curso
            matricula_actual.id_grupo = matricula.id_grupo
            matricula_actual.fecha_matricula = matricula.fecha_matricula
            session.commit()
            return matricula_actual
        finally:
            session.close()

    def eliminar_matricula(self, id_matricula: int) -> bool:
        session = get_session()
        try:
            matricula = (
                session.query(Matricula)
                .filter_by(id_matricula=id_matricula)
                .first()
            )
            if matricula is None:
                return False

            session.delete(matricula)
            session.commit()
            return True
        finally:
            session.close()

    def listar_matriculas(self) -> list[Matricula]:
        session = get_session()
        try:
            return session.query(Matricula).all()
        finally:
            session.close()