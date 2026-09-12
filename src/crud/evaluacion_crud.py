from src.database.conection import get_session
from src.entities.evaluacion import Evaluacion


class EvaluacionCRUD:
    def __init__(self):
        pass

    def crear_evaluacion(self, evaluacion: Evaluacion) -> Evaluacion:
        session = get_session()
        try:
            if (
                session.query(Evaluacion)
                .filter_by(id_evaluacion=evaluacion.id_evaluacion)
                .first()
                is not None
            ):
                raise ValueError("Ya existe una evaluación con ese ID.")

            session.add(evaluacion)
            session.commit()
            return evaluacion
        finally:
            session.close()

    def obtener_evaluacion(self, id_evaluacion: int) -> Evaluacion | None:
        session = get_session()
        try:
            return (
                session.query(Evaluacion)
                .filter_by(id_evaluacion=id_evaluacion)
                .first()
            )
        finally:
            session.close()

    def actualizar_evaluacion(
        self, id_evaluacion: int, evaluacion: Evaluacion
    ) -> Evaluacion | None:
        session = get_session()
        try:
            evaluacion_actual = (
                session.query(Evaluacion)
                .filter_by(id_evaluacion=id_evaluacion)
                .first()
            )
            if evaluacion_actual is None:
                return None

            if (
                evaluacion.id_evaluacion != id_evaluacion
                and session.query(Evaluacion)
                .filter_by(id_evaluacion=evaluacion.id_evaluacion)
                .first()
                is not None
            ):
                raise ValueError("El nuevo ID ya pertenece a otra evaluación.")

            evaluacion_actual.id_evaluacion = evaluacion.id_evaluacion
            evaluacion_actual.nombre = evaluacion.nombre
            evaluacion_actual.descripcion = evaluacion.descripcion
            evaluacion_actual.tipo = evaluacion.tipo
            evaluacion_actual.id_grupo = evaluacion.id_grupo
            evaluacion_actual.fecha = evaluacion.fecha
            evaluacion_actual.valor_maximo = evaluacion.valor_maximo
            session.commit()
            return evaluacion_actual
        finally:
            session.close()

    def eliminar_evaluacion(self, id_evaluacion: int) -> bool:
        session = get_session()
        try:
            evaluacion = (
                session.query(Evaluacion)
                .filter_by(id_evaluacion=id_evaluacion)
                .first()
            )
            if evaluacion is None:
                return False

            session.delete(evaluacion)
            session.commit()
            return True
        finally:
            session.close()

    def listar_evaluaciones(self) -> list[Evaluacion]:
        session = get_session()
        try:
            return session.query(Evaluacion).all()
        finally:
            session.close()