from src.entities.facultad import Facultad


class FacultadCRUD:
    def __init__(self):
        self.facultades = []

    def crear(self, facultad: Facultad) -> Facultad:
        if self.obtener(facultad.id_facultad) is not None:
            raise ValueError("Ya existe una facultad con ese ID.")

        self.facultades.append(facultad)
        return facultad

    def obtener(self, id_facultad: int) -> Facultad | None:
        for facultad in self.facultades:
            if facultad.id_facultad == id_facultad:
                return facultad

        return None

    def actualizar(self, id_facultad: int, facultad: Facultad) -> Facultad | None:

        for i, facultad_actual in enumerate(self.facultades):
            if facultad_actual.id_facultad == id_facultad:

                if (
                    facultad.id_facultad != id_facultad
                    and self.obtener(facultad.id_facultad) is not None
                ):
                    raise ValueError("El nuevo ID ya pertenece a otra facultad.")

                self.facultades[i] = facultad
                return facultad

        return None

    def eliminar(self, id_facultad: int) -> bool:
        facultad = self.obtener(id_facultad)

        if facultad is None:
            return False

        self.facultades.remove(facultad)
        return True

    def listar_facultades(self) -> list[Facultad]:
        return self.facultades.copy()
