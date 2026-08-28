from src.entities.estudiante import Estudiante

estudiantes: list[Estudiante] = []

def crear_estudiante(id: int, nombre: str, apellido: str, correo: str, id_estudiante: int) -> Estudiante:
    est = Estudiante(id, nombre, apellido, correo, id_estudiante)
    estudiantes.append(est)
    return est

def listar_estudiantes() -> list[Estudiante]:
    return estudiantes

def obtener_estudiante(id_estudiante: int) -> Estudiante | None:
    return next((e for e in estudiantes if e.id_estudiante == id_estudiante), None)

def actualizar_estudiante(id_estudiante: int, **kwargs) -> Estudiante | None:
    est = obtener_estudiante(id_estudiante)
    if est:
        for key, value in kwargs.items():
            setattr(est, key, value)
    return est

def eliminar_estudiante(id_estudiante: int) -> Estudiante | None:
    est = obtener_estudiante(id_estudiante)
    if est:
        estudiantes.remove(est)
    return est