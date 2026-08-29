from src.entities.curso import Curso


class CursoCRUD:
    def __init__(self):
        self.cursos = []

    def crear_curso(self, curso: Curso) -> Curso:
        if self.obtener_curso(curso.id_curso) is not None:
            raise ValueError("Ya existe un curso con ese ID.")

        self.cursos.append(curso)
        return curso

    def obtener_curso(self, id_curso: int) -> Curso | None:
        for curso in self.cursos:
            if curso.id_curso == id_curso:
                return curso

        return None

    def actualizar_curso(self, id_curso: int, curso: Curso) -> Curso | None:

        for i, curso_actual in enumerate(self.cursos):
            if curso_actual.id_curso == id_curso:

                if (
                    curso.id_curso != id_curso
                    and self.obtener_curso(curso.id_curso) is not None
                ):
                    raise ValueError("El nuevo ID ya pertenece a otro curso.")

                self.cursos[i] = curso
                return curso

        return None

    def eliminar_curso(self, id_curso: int) -> bool:
        curso = self.obtener_curso(id_curso)

        if curso is None:
            return False

        self.cursos.remove(curso)
        return True

    def listar_cursos(self) -> list[Curso]:
        return self.cursos.copy()
