from src.entities.grupo import Grupo


class GrupoCRUD:
    def __init__(self):
        self.grupos = []

    def crear_grupo(self, grupo: Grupo) -> Grupo:
        if self.obtener_grupo(grupo.id_grupo) is not None:
            raise ValueError("Ya existe un grupo con ese ID.")

        self.grupos.append(grupo)
        return grupo

    def obtener_grupo(self, id_grupo: int) -> Grupo | None:
        for grupo in self.grupos:
            if grupo.id_grupo == id_grupo:
                return grupo

        return None

    def actualizar_grupo(self, id_grupo: int, grupo: Grupo) -> Grupo | None:

        for i, grupo_actual in enumerate(self.grupos):
            if grupo_actual.id_grupo == id_grupo:

                if (
                    grupo.id_grupo != id_grupo
                    and self.obtener_grupo(grupo.id_grupo) is not None
                ):
                    raise ValueError("El nuevo ID ya pertenece a otro grupo.")

                self.grupos[i] = grupo
                return grupo

        return None

    def eliminar_grupo(self, id_grupo: int) -> bool:
        grupo = self.obtener_grupo(id_grupo)

        if grupo is None:
            return False

        self.grupos.remove(grupo)
        return True

    def listar_grupos(self) -> list[Grupo]:
        return self.grupos.copy()
