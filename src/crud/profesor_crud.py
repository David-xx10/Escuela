from src.database.conection import get_session
from src.entities.profesor import Profesor


class ProfesorCRUD:
    def __init__(self):
        self.db = get_session()

    def crear(self, profesor: Profesor) -> Profesor:
        if self.obtener(profesor.id_profesor) is not None:
            raise ValueError("Ya existe un profesor con ese ID.")
        self.db.add(profesor)
        self.db.commit()
        self.db.refresh(profesor)
        return profesor

    def obtener(self, id_profesor: int) -> Profesor | None:
        return self.db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()

    def actualizar(self, id_profesor: int, profesor: Profesor) -> Profesor | None:
        actual = self.obtener(id_profesor)
        if actual is None:
            return None
        actual.nombre = profesor.nombre
        actual.apellido = profesor.apellido
        actual.correo = profesor.correo
        self.db.commit()
        self.db.refresh(actual)
        return actual

    def eliminar(self, id_profesor: int) -> bool:
        profesor = self.obtener(id_profesor)
        if profesor is None:
            return False
        self.db.delete(profesor)
        self.db.commit()
        return True

    def listar_profesores(self) -> list[Profesor]:
        return self.db.query(Profesor).all()
