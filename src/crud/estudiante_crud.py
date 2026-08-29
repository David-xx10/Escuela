from src.entities.estudiante import Estudiante


class EstudianteCRUD:
    def __init__(self):
        self.estudiantes = []

    def crear_estudiante(self, estudiante: Estudiante) -> Estudiante:
        if self.obtener_estudiante(estudiante.id_estudiante) is not None:
            raise ValueError("Ya existe un estudiante con ese ID.")
        self.estudiantes.append(estudiante)
        return estudiante

    def obtener_estudiante(self, id_estudiante: int) -> Estudiante | None:
        for estudiante in self.estudiantes:
            if estudiante.id_estudiante == id_estudiante:
                return estudiante
        return None

    def actualizar_estudiante(
        self, id_estudiante: int, estudiante: Estudiante
    ) -> Estudiante | None:
        for i, est_actual in enumerate(self.estudiantes):
            if est_actual.id_estudiante == id_estudiante:
                if (
                    estudiante.id_estudiante != id_estudiante
                    and self.obtener_estudiante(estudiante.id_estudiante) is not None
                ):
                    raise ValueError("El nuevo ID ya pertenece a otro estudiante.")
                self.estudiantes[i] = estudiante
                return estudiante
        return None

    def eliminar_estudiante(self, id_estudiante: int) -> bool:
        estudiante = self.obtener_estudiante(id_estudiante)
        if estudiante is None:
            return False
        self.estudiantes.remove(estudiante)
        return True

    def listar_estudiantes(self) -> list[Estudiante]:
        return self.estudiantes.copy()
