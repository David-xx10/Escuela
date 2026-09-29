from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.cursos import router as cursos_router
from src.api.evaluacion import router as evaluaciones_router
from src.api.facultades import router as facultades_router
from src.api.grupos import router as grupos_router
from src.api.matriculas import router as matriculas_router
from src.api.periodo_academico import router as periodos_academicos_router


app = FastAPI(
    title="Sistema de Gestión Escolar",
    description="API REST para la gestión de facultades, cursos, grupos, matrículas, evaluaciones y periodos académicos.",
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
app.include_router(matriculas_router)
app.include_router(evaluaciones_router)
app.include_router(periodos_academicos_router)


@app.get("/")
def estado_salud() -> dict[str, str]:
    return {"mensaje": "API REST activa y funcionando"}
