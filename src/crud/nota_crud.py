from src.entities.nota import Nota


class NotaCRUD:
    def __init__(self):
        self.notas = []

    def registrar_nota(self, nota: Nota) -> Nota:
        if self.obtener_nota(nota.id_nota) is not None:
            raise ValueError("Ya existe una nota con ese ID.")
        self.notas.append(nota)
        return nota

    def obtener_nota(self, id_nota: int) -> Nota | None:
        for nota in self.notas:
            if nota.id_nota == id_nota:
                return nota
        return None

    def actualizar_nota(self, id_nota: int, nota: Nota) -> Nota | None:
        for i, nota_actual in enumerate(self.notas):
            if nota_actual.id_nota == id_nota:
                if (
                    nota.id_nota != id_nota
                    and self.obtener_nota(nota.id_nota) is not None
                ):
                    raise ValueError("El nuevo ID ya pertenece a otra nota.")
                self.notas[i] = nota
                return nota
        return None

    def eliminar_nota(self, id_nota: int) -> bool:
        nota = self.obtener_nota(id_nota)
        if nota is None:
            return False
        self.notas.remove(nota)
        return True

    def listar_notas(self) -> list[Nota]:
        return self.notas.copy()

    def calcular_promedio(self, id_estudiante: int) -> float:
        notas_estudiante = [
            n.valor for n in self.notas if n.id_estudiante == id_estudiante
        ]
        if not notas_estudiante:
            return 0.0
        return sum(notas_estudiante) / len(notas_estudiante)
