class Grupo:
    def __init__(self, id_grupo: int, id_curso: int, id_profesor: int, cupo: int):
        if not isinstance(id_grupo, int) or id_grupo <= 0:
            raise ValueError("El id del grupo debe ser un entero positivo.")

        if not isinstance(id_curso, int) or id_curso <= 0:
            raise ValueError("El id del curso debe ser un entero positivo.")

        if not isinstance(id_profesor, int) or id_profesor <= 0:
            raise ValueError("El id del profesor debe ser un entero positivo.")

        if not isinstance(cupo, int) or cupo <= 0:
            raise ValueError("El cupo debe ser un entero positivo.")

        self.id_grupo = id_grupo
        self.id_curso = id_curso
        self.id_profesor = id_profesor
        self.cupo = cupo

    def __str__(self):
        return (
            f"Grupo {self.id_grupo}: "
            f"Curso {self.id_curso}, "
            f"Profesor {self.id_profesor}, "
            f"Cupo {self.cupo}"
        )
