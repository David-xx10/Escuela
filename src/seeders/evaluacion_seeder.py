from src.database.conection import get_session
from src.entities.evaluacion import Evaluacion


def seed_evaluaciones():
    datos = [
        {
            "id_evaluacion": 1,
            "nombre": "Quiz 1",
            "descripcion": "Evaluación corta de conceptos básicos",
            "tipo": "Quiz",
            "id_grupo": 1,
            "fecha": "2026-02-10",
            "valor_maximo": 5.0,
        },
        {
            "id_evaluacion": 2,
            "nombre": "Parcial 1",
            "descripcion": "Examen parcial del primer corte",
            "tipo": "Parcial",
            "id_grupo": 1,
            "fecha": "2026-03-05",
            "valor_maximo": 10.0,
        },
        {
            "id_evaluacion": 3,
            "nombre": "Taller final",
            "descripcion": "Actividad práctica de cierre del curso",
            "tipo": "Taller",
            "id_grupo": 1,
            "fecha": "2026-04-20",
            "valor_maximo": 20.0,
        },
    ]

    session = get_session()
    try:
        for item in datos:
            evaluacion = (
                session.query(Evaluacion)
                .filter_by(id_evaluacion=item["id_evaluacion"])
                .first()
            )
            if evaluacion is None:
                session.add(Evaluacion(**item))

        session.commit()
        print("Seed temporal de evaluaciones ejecutado.")
    finally:
        session.close()


if __name__ == "__main__":
    seed_evaluaciones()
