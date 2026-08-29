from src.entities.persona import Persona


class Estudiante(Persona):
    def __init__(self, id_persona: int, nombre: str, apellido: str, correo: str, id_estudiante: int):
        super().__init__(id_persona, nombre, apellido, correo)
        
        if not isinstance(id_estudiante, int) or id_estudiante <= 0:
            raise ValueError("El id del estudiante debe ser un entero positivo.")
        
        self.id_estudiante = id_estudiante

    def __str__(self) -> str:
        return f"{super().__str__()} - Estudiante #{self.id_estudiante}"