class Facultad:
    def __init__(self, id_facultad: int, nombre: str):
        if not isinstance(id_facultad, int) or id_facultad <= 0:
            raise ValueError("El id de la facultad debe ser un entero positivo.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la facultad no puede estar vacío.")

        self.id_facultad = id_facultad
        self.nombre = nombre.strip()

    def __str__(self):
        return f"Facultad {self.id_facultad}: {self.nombre}"
