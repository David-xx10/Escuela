from src.entities.profesor import Profesor


class ProfesorCRUD:
    def __init__(self):
        self.profesores = []

    def crear(self, profesor: Profesor) -> Profesor:
        if self.obtener(profesor.id_profesor) is not None:
            raise ValueError("Ya existe un profesor con ese ID.")
        self.profesores.append(profesor)
        return profesor

    def obtener(self, id_profesor: int) -> Profesor | None:
        for profesor in self.profesores:
            if profesor.id_profesor == id_profesor:
                return profesor
        return None

    def actualizar(self, id_profesor: int, profesor: Profesor) -> Profesor | None:
        for i, prof_actual in enumerate(self.profesores):
            if prof_actual.id_profesor == id_profesor:
                if (
                    profesor.id_profesor != id_profesor
                    and self.obtener(profesor.id_profesor) is not None
                ):
                    raise ValueError("El nuevo ID ya pertenece a otro profesor.")
                self.profesores[i] = profesor
                return profesor
        return None

    def eliminar(self, id_profesor: int) -> bool:
        profesor = self.obtener(id_profesor)
        if profesor is None:
            return False
        self.profesores.remove(profesor)
        return True

    def listar_profesores(self) -> list[Profesor]:
        return self.profesores.copy()
