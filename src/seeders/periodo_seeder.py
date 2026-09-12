from src.database.conection import get_session
from src.entities.periodo_academico import PeriodoAcademico


def seed_periodos():
    datos = [{"id_periodo": 1, "nombre": "Periodo 2026-1"}]

    session = get_session()
    try:
        for item in datos:
            periodo = (
                session.query(PeriodoAcademico)
                .filter_by(id_periodo=item["id_periodo"])
                .first()
            )
            if periodo is None:
                session.add(PeriodoAcademico(**item))

        session.commit()
        print("Seed temporal de periodos ejecutado.")
    finally:
        session.close()


if __name__ == "__main__":
    seed_periodos()
