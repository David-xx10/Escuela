from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import inspect, text

from src.api.cursos import router as cursos_router
from src.api.facultades import router as facultades_router
from src.api.grupos import router as grupos_router
from src.api.estudiantes import router as estudiantes_router
from src.api.profesores import router as profesores_router
from src.api.notas import router as notas_router
from src.api.evaluacion import router as evaluaciones_router
from src.api.matriculas import router as matriculas_router
from src.api.periodo_academico import router as periodos_academicos_router
from src.database.conection import Base, engine


def crear_esquema_si_falta() -> None:
    Base.metadata.create_all(bind=engine)

    inspector = inspect(engine)
    if not inspector.has_table("periodos_academicos"):
        return

    columnas = {col["name"] for col in inspector.get_columns("periodos_academicos")}
    for columna, tipo in {
        "fecha_inicio": "VARCHAR(10)",
        "fecha_fin": "VARCHAR(10)",
        "estado": "VARCHAR(20)",
    }.items():
        if columna not in columnas:
            with engine.begin() as conexion:
                conexion.execute(text(f"ALTER TABLE periodos_academicos ADD COLUMN {columna} {tipo}"))

    with engine.begin() as conexion:
        conexion.execute(
            text(
                "UPDATE periodos_academicos SET fecha_inicio = COALESCE(fecha_inicio, '2000-01-01'), "
                "fecha_fin = COALESCE(fecha_fin, '2000-12-31'), "
                "estado = COALESCE(estado, 'activo') "
                "WHERE fecha_inicio IS NULL OR fecha_fin IS NULL OR estado IS NULL"
            )
        )


crear_esquema_si_falta()


app = FastAPI(
    title="Sistema de Gestión Escolar",
    description="API REST para la gestión de facultades, cursos, grupos, matriculas, evaluaciones, periodos academicos, estudiantes, profesores y notas.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(facultades_router)
app.include_router(cursos_router)
app.include_router(grupos_router)
app.include_router(estudiantes_router)
app.include_router(profesores_router)
app.include_router(notas_router)
app.include_router(matriculas_router)
app.include_router(evaluaciones_router)
app.include_router(periodos_academicos_router)


@app.get("/")
def estado_salud() -> dict[str, str]:
    return {"mensaje": "API REST activa y funcionando"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
