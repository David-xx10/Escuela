class Curso:
    def __init__(self, id_curso: int, nombre: str, creditos: int, id_facultad: int):
        if not isinstance(id_curso, int) or id_curso <= 0:
            raise ValueError("El id del curso debe ser un entero positivo.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del curso no puede estar vacío.")

        if not isinstance(creditos, int) or creditos <= 0:
            raise ValueError("Los créditos deben ser un entero positivo.")

        if not isinstance(id_facultad, int) or id_facultad <= 0:
            raise ValueError("El id de la facultad debe ser un entero positivo.")

        self.id_curso = id_curso
        self.nombre = nombre.strip()
        self.creditos = creditos
        self.id_facultad = id_facultad

    def __str__(self):
        return f"Curso {self.id_curso}: {self.nombre} " f"({self.creditos} créditos)"
