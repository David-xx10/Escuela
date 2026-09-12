from src.crud.facultad_crud import FacultadCRUD
from src.entities.facultad import Facultad


def seed_facultades():
    crud = FacultadCRUD()
    datos = [
        {"id_facultad": 1, "nombre": "Ingeniería"},
        {"id_facultad": 2, "nombre": "Ciencias Exactas"},
    ]
    for item in datos:
        crud.crear_facultad(
            Facultad(id_facultad=item["id_facultad"], nombre=item["nombre"])
        )
    print("Seed de facultades ejecutado.")


if __name__ == "__main__":
    seed_facultades()
