from src.entities.matricula import Matricula

class MatriculaCRUD:
    def __init__(self):
        self.matriculas = []

    def crear_matricula(self, matricula: Matricula) -> Matricula:
        if self.obtener_matricula(matricula.id_matricula) is not None:
            raise ValueError("Ya existe una matrícula con ese ID.")

        self.matriculas.append(matricula)
        return matricula

    def obtener_matricula(self, id_matricula: int) -> Matricula | None:
        for matricula in self.matriculas:
            if matricula.id_matricula == id_matricula:
                return matricula

        return None

    def actualizar_matricula(self, id_matricula: int, matricula: Matricula) -> Matricula | None:
        for i, matricula_actual in enumerate(self.matriculas):
            if matricula_actual.id_matricula == id_matricula:

                if (
                    matricula.id_matricula != id_matricula
                    and self.obtener_matricula(matricula.id_matricula) is not None
                ):
                    raise ValueError("El nuevo ID ya pertenece a otra matrícula.")

                self.matriculas[i] = matricula
                return matricula

        return None

    def eliminar_matricula(self, id_matricula: int) -> bool:
        matricula = self.obtener_matricula(id_matricula)

        if matricula is None:
            return False

        self.matriculas.remove(matricula)
        return True

    def listar_matriculas(self) -> list[Matricula]:
        return self.matriculas.copy()