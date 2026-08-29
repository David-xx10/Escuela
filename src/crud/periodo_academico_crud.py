from src.entities.periodo_academico import PeriodoAcademico


periodos_academicos: list[PeriodoAcademico] = []


def crear_periodo_academico(
    id_periodo_academico: int,
    nombre: str,
    fecha_inicio: str,
    fecha_fin: str
) -> PeriodoAcademico:
    periodo = PeriodoAcademico(id_periodo_academico, nombre, fecha_inicio, fecha_fin)
    periodos_academicos.append(periodo)
    return periodo


def listar_periodos_academicos() -> list[PeriodoAcademico]:
    return periodos_academicos


def obtener_periodo_academico(id_periodo_academico: int) -> PeriodoAcademico | None:
    return next(
        (p for p in periodos_academicos if p.id_periodo_academico == id_periodo_academico),
        None
    )


def actualizar_periodo_academico(
    id_periodo_academico: int,
    **kwargs
) -> PeriodoAcademico | None:
    periodo = obtener_periodo_academico(id_periodo_academico)
    if periodo:
        for key, value in kwargs.items():
            setattr(periodo, key, value)
    return periodo


def eliminar_periodo_academico(id_periodo_academico: int) -> PeriodoAcademico | None:
    periodo = obtener_periodo_academico(id_periodo_academico)
    if periodo:
        periodos_academicos.remove(periodo)
    return periodo