class Persona:
    def __init__(self, id_persona: int, nombre: str, apellido: str, correo: str):
        if not isinstance(id_persona, int) or id_persona <= 0:
            raise ValueError("El id de la persona debe ser un entero positivo.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre de la persona no puede estar vacío.")

        if not isinstance(apellido, str) or not apellido.strip():
            raise ValueError("El apellido de la persona no puede estar vacío.")

        if not isinstance(correo, str) or not correo.strip():
            raise ValueError("El correo de la persona no puede estar vacío.")

        self.id_persona = id_persona
        self.nombre = nombre.strip()
        self.apellido = apellido.strip()
        self.correo = correo.strip()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} ({self.correo})"
