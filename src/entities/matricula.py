class Matricula: 
    def __init__(self, id_matricula: int, id_estudiante: int, id_curso: int, fecha_matricula: str):
        if not isinstance(id_matricula, int) or id_matricula <= 0:
            raise ValueError("El id de la matricula debe ser un número entero positivo.")
        if not isinstance(id_estudiante, int) or id_estudiante <= 0:
            raise ValueError("El id del estudiante debe ser un número entero positivo.")
        if not isinstance(id_curso, int) or id_curso <= 0:
            raise ValueError("El id del curso debe ser un número entero positivo.")
        if not isinstance(fecha_matricula, str):
            raise ValueError("La fecha de matrícula debe ser una cadena de texto.")

        self.id_matricula = id_matricula
        self.id_alumno = id_estudiante
        self.id_curso = id_curso
        self.fecha_matricula = fecha_matricula