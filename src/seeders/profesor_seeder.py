from src.database.conection import get_session
from src.entities.profesor import Profesor


def seed_profesores():
    datos = [
        {
            "id_profesor": 1,
            "nombre": "Carlos",
            "apellido": "Gomez",
            "correo": "carlos.gomez@universidad.edu",
        }
    ]

    session = get_session()
    try:
        for item in datos:
            profesor = (
                session.query(Profesor)
                .filter_by(id_profesor=item["id_profesor"])
                .first()
            )
            if profesor is None:
                session.add(Profesor(**item))

        session.commit()
        print("Seed temporal de profesores ejecutado.")
    finally:
        session.close()


if __name__ == "__main__":
    seed_profesores()
