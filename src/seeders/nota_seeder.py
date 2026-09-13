from src.database.conection import get_session
from src.entities.nota import Nota


def seed_notas():
    datos = [
        {"id_nota": 1, "id_estudiante": 1, "id_evaluacion": 1, "valor": 4.5},
        {"id_nota": 2, "id_estudiante": 1, "id_evaluacion": 2, "valor": 3.8},
    ]

    session = get_session()
    try:
        for item in datos:
            nota = session.query(Nota).filter_by(id_nota=item["id_nota"]).first()
            if nota is None:
                session.add(Nota(**item))

        session.commit()
        print("Seed temporal de notas ejecutado.")
    finally:
        session.close()


if __name__ == "__main__":
    seed_notas()