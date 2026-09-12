from src.database.conection import get_session
from src.entities.grupo import Grupo


class GrupoCRUD:
    def __init__(self):
        pass

    def crear_grupo(self, grupo: Grupo) -> Grupo:
        session = get_session()
        try:
            if (
                session.query(Grupo).filter_by(id_grupo=grupo.id_grupo).first()
                is not None
            ):
                raise ValueError("Ya existe un grupo con ese ID.")

            session.add(grupo)
            session.commit()
            return grupo
        finally:
            session.close()

    def obtener_grupo(self, id_grupo: int) -> Grupo | None:
        session = get_session()
        try:
            return session.query(Grupo).filter_by(id_grupo=id_grupo).first()
        finally:
            session.close()

    def actualizar_grupo(self, id_grupo: int, grupo: Grupo) -> Grupo | None:
        session = get_session()
        try:
            grupo_actual = session.query(Grupo).filter_by(id_grupo=id_grupo).first()
            if grupo_actual is None:
                return None

            if (
                grupo.id_grupo != id_grupo
                and session.query(Grupo).filter_by(id_grupo=grupo.id_grupo).first()
                is not None
            ):
                raise ValueError("El nuevo ID ya pertenece a otro grupo.")

            grupo_actual.id_grupo = grupo.id_grupo
            grupo_actual.id_curso = grupo.id_curso
            grupo_actual.id_profesor = grupo.id_profesor
            grupo_actual.id_periodo = grupo.id_periodo
            grupo_actual.cupo = grupo.cupo
            session.commit()
            return grupo_actual
        finally:
            session.close()

    def eliminar_grupo(self, id_grupo: int) -> bool:
        session = get_session()
        try:
            grupo = session.query(Grupo).filter_by(id_grupo=id_grupo).first()
            if grupo is None:
                return False

            session.delete(grupo)
            session.commit()
            return True
        finally:
            session.close()

    def listar_grupos(self) -> list[Grupo]:
        session = get_session()
        try:
            return session.query(Grupo).all()
        finally:
            session.close()
