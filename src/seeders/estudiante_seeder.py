from src.database.conection import get_session
from src.entities.estudiante import Estudiante


def seed_estudiantes():
    datos = [
        {
            "id_estudiante": 1,
            "nombre": "Pablo",
            "apellido": "Suarez",
            "correo": "pablo.suarez@universidad.edu",
        },
        {
            "id_estudiante": 2,
            "nombre": "Laura",
            "apellido": "Gomez",
            "correo": "laura.gomez@universidad.edu",
        },
    ]

    session = get_session()
    try:
        for item in datos:
            estudiante = (
                session.query(Estudiante)
                .filter_by(id_estudiante=item["id_estudiante"])
                .first()
            )
            if estudiante is None:
                session.add(Estudiante(**item))

        session.commit()
        print("Seed temporal de estudiantes ejecutado.")
    finally:
        session.close()


if __name__ == "__main__":
    seed_estudiantes()