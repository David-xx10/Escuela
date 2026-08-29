from src.entities.evaluacion import Evaluacion


class EvaluacionCRUD:
    def __init__(self):
        self.evaluaciones = []

    def crear_evaluacion(self, evaluacion: Evaluacion) -> Evaluacion:
        if self.obtener_evaluacion(evaluacion.id_evaluacion) is not None:
            raise ValueError("Ya existe una evaluación con ese ID.")

        self.evaluaciones.append(evaluacion)
        return evaluacion

    def obtener_evaluacion(self, id_evaluacion: int) -> Evaluacion | None:
        for evaluacion in self.evaluaciones:
            if evaluacion.id_evaluacion == id_evaluacion:
                return evaluacion

        return None

    def actualizar_evaluacion(
        self, id_evaluacion: int, evaluacion: Evaluacion
    ) -> Evaluacion | None:
        for i, evaluacion_actual in enumerate(self.evaluaciones):
            if evaluacion_actual.id_evaluacion == id_evaluacion:
                if (
                    evaluacion.id_evaluacion != id_evaluacion
                    and self.obtener_evaluacion(evaluacion.id_evaluacion) is not None
                ):
                    raise ValueError("El nuevo ID ya pertenece a otra evaluación.")

                self.evaluaciones[i] = evaluacion
                return evaluacion

        return None

    def eliminar_evaluacion(self, id_evaluacion: int) -> bool:
        evaluacion = self.obtener_evaluacion(id_evaluacion)

        if evaluacion is None:
            return False

        self.evaluaciones.remove(evaluacion)
        return True

    def listar_evaluaciones(self) -> list[Evaluacion]:
        return self.evaluaciones.copy()