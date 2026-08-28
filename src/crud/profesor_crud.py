from src.entities.profesor import Profesor

profesores: list[Profesor] = []

def crear_profesor(id: int, nombre: str, apellido: str, correo: str, id_profesor: int) -> Profesor:
    prof = Profesor(id, nombre, apellido, correo, id_profesor)
    profesores.append(prof)
    return prof

def listar_profesores() -> list[Profesor]:
    return profesores

def obtener_profesor(id_profesor: int) -> Profesor | None:
    return next((p for p in profesores if p.id_profesor == id_profesor), None)

def actualizar_profesor(id_profesor: int, **kwargs) -> Profesor | None:
    prof = obtener_profesor(id_profesor)
    if prof:
        for key, value in kwargs.items():
            setattr(prof, key, value)
    return prof

def eliminar_profesor(id_profesor: int) -> Profesor | None:
    prof = obtener_profesor(id_profesor)
    if prof:
        profesores.remove(prof)
    return prof