from src.crud.grupo_crud import GrupoCRUD
from src.entities.grupo import Grupo


def seed_grupos():
    crud = GrupoCRUD()
    datos = [
        {
            "id_grupo": 1,
            "id_curso": 101,
            "id_profesor": 1,
            "id_periodo": 1,
            "cupo": 30,
        },
    ]
    for item in datos:
        crud.crear_grupo(
            Grupo(
                id_grupo=item["id_grupo"],
                id_curso=item["id_curso"],
                id_profesor=item["id_profesor"],
                id_periodo=item["id_periodo"],
                cupo=item["cupo"],
            )
        )
    print("Seed de grupos ejecutado.")


if __name__ == "__main__":
    seed_grupos()
