from src.database.conection import get_session
from src.entities.periodo_academico import PeriodoAcademico


class PeriodoAcademicoCRUD:
    def __init__(self):
        pass

    def crear_periodo_academico(self, periodo: PeriodoAcademico) -> PeriodoAcademico:
        session = get_session()
        try:
            if (
                session.query(PeriodoAcademico)
                .filter_by(id_periodo=periodo.id_periodo)
                .first()
                is not None
            ):
                raise ValueError("Ya existe un periodo académico con ese ID.")

            session.add(periodo)
            session.commit()
            return periodo
        finally:
            session.close()

    def obtener_periodo_academico(self, id_periodo: int) -> PeriodoAcademico | None:
        session = get_session()
        try:
            return session.query(PeriodoAcademico).filter_by(id_periodo=id_periodo).first()
        finally:
            session.close()

    def actualizar_periodo_academico(
        self, id_periodo: int, periodo: PeriodoAcademico
    ) -> PeriodoAcademico | None:
        session = get_session()
        try:
            periodo_actual = (
                session.query(PeriodoAcademico)
                .filter_by(id_periodo=id_periodo)
                .first()
            )
            if periodo_actual is None:
                return None

            if (
                periodo.id_periodo != id_periodo
                and session.query(PeriodoAcademico)
                .filter_by(id_periodo=periodo.id_periodo)
                .first()
                is not None
            ):
                raise ValueError("El nuevo ID ya pertenece a otro periodo académico.")

            periodo_actual.id_periodo = periodo.id_periodo
            periodo_actual.nombre = periodo.nombre
            session.commit()
            return periodo_actual
        finally:
            session.close()

    def eliminar_periodo_academico(self, id_periodo: int) -> bool:
        session = get_session()
        try:
            periodo = session.query(PeriodoAcademico).filter_by(id_periodo=id_periodo).first()
            if periodo is None:
                return False

            session.delete(periodo)
            session.commit()
            return True
        finally:
            session.close()

    def listar_periodos_academicos(self) -> list[PeriodoAcademico]:
        session = get_session()
        try:
            return session.query(PeriodoAcademico).all()
        finally:
            session.close()