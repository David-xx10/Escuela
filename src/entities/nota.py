class Nota:
    def __init__(
        self, id_nota: int, id_estudiante: int, id_evaluacion: int, valor: float
    ):
        if not isinstance(id_nota, int) or id_nota <= 0:
            raise ValueError("El id de la nota debe ser un entero positivo.")

        if not isinstance(id_estudiante, int) or id_estudiante <= 0:
            raise ValueError("El id del estudiante debe ser un entero positivo.")

        if not isinstance(id_evaluacion, int) or id_evaluacion <= 0:
            raise ValueError("El id de la evaluación debe ser un entero positivo.")

        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El valor de la nota debe ser un número no negativo.")

        self.id_nota = id_nota
        self.id_estudiante = id_estudiante
        self.id_evaluacion = id_evaluacion
        self.valor = valor

    def __str__(self) -> str:
        return f"Nota #{self.id_nota} - Estudiante {self.id_estudiante} - Valor: {self.valor}"
