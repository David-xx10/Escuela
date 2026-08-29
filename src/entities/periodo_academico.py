class PeriodoAcademico:
    def __init__(self, id_periodo_academico: int, nombre: str, fecha_inicio: str, fecha_fin: str):
        if not isinstance(id_periodo_academico, int) or id_periodo_academico <= 0:
            raise ValueError("El id del periodo académico debe ser un entero positivo.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del periodo académico no puede estar vacío.")

        if not isinstance(fecha_inicio, str) or not fecha_inicio.strip():
            raise ValueError("La fecha de inicio no puede estar vacía.")

        if not isinstance(fecha_fin, str) or not fecha_fin.strip():
            raise ValueError("La fecha de fin no puede estar vacía.")

        self.id_periodo_academico = id_periodo_academico
        self.nombre = nombre.strip()
        self.fecha_inicio = fecha_inicio.strip()
        self.fecha_fin = fecha_fin.strip()

    def __str__(self):
        return f"Periodo {self.id_periodo_academico}: {self.nombre} ({self.fecha_inicio} - {self.fecha_fin})"