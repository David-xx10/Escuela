from src.database.conection import get_session
from src.entities.matricula import Matricula


def seed_matriculas():
    datos = [
        {
            "id_matricula": 1,
            "id_estudiante": 1001,
            "id_curso": 101,
            "id_grupo": 1,
            "fecha_matricula": "2026-01-15",
        },
        {
            "id_matricula": 2,
            "id_estudiante": 1002,
            "id_curso": 102,
            "id_grupo": 1,
            "fecha_matricula": "2026-01-16",
        },
        {
            "id_matricula": 3,
            "id_estudiante": 1003,
            "id_curso": 101,
            "id_grupo": None,
            "fecha_matricula": "2026-01-17",
        },
    ]

    session = get_session()
    try:
        for item in datos:
            matricula = (
                session.query(Matricula)
                .filter_by(id_matricula=item["id_matricula"])
                .first()
            )
            if matricula is None:
                session.add(Matricula(**item))

        session.commit()
        print("Seed temporal de matrículas ejecutado.")
    finally:
        session.close()


if __name__ == "__main__":
    seed_matriculas()
