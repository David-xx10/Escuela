from src.entities.persona import Persona

class Estudiante(Persona):
    def __init__(self, id: int, nombre: str, apellido: str, correo: str, id_estudiante: int):
        super().__init__(id, nombre, apellido, correo)
        self.id_estudiante = id_estudiante

    def __str__(self) -> str:
        return f"{super().__str__()} - Estudiante #{self.id_estudiante}"