from src.database.conection import get_session
from src.entities.nota import Nota


class NotaCRUD:
    def __init__(self):
        self.db = get_session()

    def registrar_nota(self, nota: Nota) -> Nota:
        if self.obtener_nota(nota.id_nota) is not None:
            raise ValueError("Ya existe una nota con ese ID.")
        self.db.add(nota)
        self.db.commit()
        self.db.refresh(nota)
        return nota

    def obtener_nota(self, id_nota: int) -> Nota | None:
        return self.db.query(Nota).filter(Nota.id_nota == id_nota).first()

    def actualizar_nota(self, id_nota: int, nota: Nota) -> Nota | None:
        actual = self.obtener_nota(id_nota)
        if actual is None:
            return None
        actual.id_estudiante = nota.id_estudiante
        actual.id_evaluacion = nota.id_evaluacion
        actual.valor = nota.valor
        self.db.commit()
        self.db.refresh(actual)
        return actual

    def eliminar_nota(self, id_nota: int) -> bool:
        nota = self.obtener_nota(id_nota)
        if nota is None:
            return False
        self.db.delete(nota)
        self.db.commit()
        return True

    def listar_notas(self) -> list[Nota]:
        return self.db.query(Nota).all()

    def calcular_promedio(self, id_estudiante: int) -> float:
        notas = self.db.query(Nota).filter(Nota.id_estudiante == id_estudiante).all()
        if not notas:
            return 0.0
        return sum(n.valor for n in notas) / len(notas)
