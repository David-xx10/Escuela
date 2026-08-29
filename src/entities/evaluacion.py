class Evaluacion:
    def __init__(self, id_evaluacion: int, nombre: str, descripcion: str, tipo: str, id_grupo: int, fecha: str, valor_maximo: float):
        if not isinstance(id_evaluacion, int) or id_evaluacion <= 0:
            raise ValueError("El id de la evaluación debe ser un número entero positivo.")
        if not isinstance(nombre, str):
            raise ValueError("El nombre de la evaluación debe ser una cadena de texto.")
        if not isinstance(descripcion, str):
            raise ValueError("La descripción debe ser una cadena de texto.")
        if not isinstance(tipo, str):
            raise ValueError("El tipo de evaluación debe ser una cadena de texto.")
        if not isinstance(id_grupo, int) or id_grupo <= 0:
            raise ValueError("El id del grupo debe ser un número entero positivo.")
        if not isinstance(fecha, str):
            raise ValueError("La fecha debe ser una cadena de texto.")
        if not isinstance(valor_maximo, (int, float)) or valor_maximo <= 0:
            raise ValueError("El valor máximo debe ser un número positivo.")

        self.id_evaluacion = id_evaluacion
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
        self.id_grupo = id_grupo
        self.fecha = fecha
        self.valor_maximo = valor_maximo

    def __str__(self) -> str:
        return f"Evaluación #{self.id_evaluacion} - {self.nombre} ({self.tipo}) - Grupo {self.id_grupo} - Fecha: {self.fecha} - Valor máximo: {self.valor_maximo}"