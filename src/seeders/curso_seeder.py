from src.crud.curso_crud import CursoCRUD
from src.entities.curso import Curso


def seed_cursos():
    crud = CursoCRUD()
    datos = [
        {
            "id_curso": 101,
            "nombre": "Programación Orientada a Objetos",
            "creditos": 3,
            "id_facultad": 1,
        },
        {"id_curso": 102, "nombre": "Bases de Datos", "creditos": 4, "id_facultad": 1},
    ]
    for item in datos:
        crud.crear_curso(
            Curso(
                id_curso=item["id_curso"],
                nombre=item["nombre"],
                creditos=item["creditos"],
                id_facultad=item["id_facultad"],
            )
        )
    print("Seed de cursos ejecutado.")


if __name__ == "__main__":
    seed_cursos()
