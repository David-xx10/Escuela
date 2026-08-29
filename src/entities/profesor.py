from src.entities.persona import Persona

class Profesor(Persona):
    def __init__(self, id: int, nombre: str, apellido: str, correo: str, id_profesor: int):
        super().__init__(id, nombre, apellido, correo)
        self.id_profesor = id_profesor

    def __str__(self) -> str:
        return f"{super().__str__()} - Profesor #{self.id_profesor}"