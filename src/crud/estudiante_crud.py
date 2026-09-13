from src.database.conection import get_session
from src.entities.estudiante import Estudiante


class EstudianteCRUD:
    def __init__(self):
        self.db = get_session()

    def crear_estudiante(self, estudiante: Estudiante) -> Estudiante:
        if self.obtener_estudiante(estudiante.id_estudiante) is not None:
            raise ValueError("Ya existe un estudiante con ese ID.")
        self.db.add(estudiante)
        self.db.commit()
        self.db.refresh(estudiante)
        return estudiante

    def obtener_estudiante(self, id_estudiante: int) -> Estudiante | None:
        return self.db.query(Estudiante).filter(Estudiante.id_estudiante == id_estudiante).first()

    def actualizar_estudiante(self, id_estudiante: int, estudiante: Estudiante) -> Estudiante | None:
        actual = self.obtener_estudiante(id_estudiante)
        if actual is None:
            return None
        actual.nombre = estudiante.nombre
        actual.apellido = estudiante.apellido
        actual.correo = estudiante.correo
        self.db.commit()
        self.db.refresh(actual)
        return actual

    def eliminar_estudiante(self, id_estudiante: int) -> bool:
        estudiante = self.obtener_estudiante(id_estudiante)
        if estudiante is None:
            return False
        self.db.delete(estudiante)
        self.db.commit()
        return True

    def listar_estudiantes(self) -> list[Estudiante]:
        return self.db.query(Estudiante).all()
