class Nota:
    def __init__(self, id_nota: int, id_estudiante: int, id_evaluacion: int, valor: float):
        self.id_nota = id_nota
        self.id_estudiante = id_estudiante
        self.id_evaluacion = id_evaluacion
        self.valor = valor

    def __str__(self) -> str:
        return f"Nota #{self.id_nota} - Estudiante {self.id_estudiante} - Valor: {self.valor}"