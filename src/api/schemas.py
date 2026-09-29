from typing import Optional

from pydantic import BaseModel, ConfigDict


class FacultadCreate(BaseModel):
    nombre: str


class FacultadUpdate(BaseModel):
    nombre: Optional[str] = None


class FacultadResponse(BaseModel):
    id_facultad: int
    nombre: str

    model_config = ConfigDict(from_attributes=True)


class CursoCreate(BaseModel):
    nombre: str
    creditos: int
    id_facultad: int


class CursoUpdate(BaseModel):
    nombre: Optional[str] = None
    creditos: Optional[int] = None
    id_facultad: Optional[int] = None


class CursoResponse(BaseModel):
    id_curso: int
    nombre: str
    creditos: int
    id_facultad: int

    model_config = ConfigDict(from_attributes=True)


class GrupoCreate(BaseModel):
    id_curso: int
    id_profesor: int
    id_periodo: int
    cupo: int


class GrupoUpdate(BaseModel):
    id_curso: Optional[int] = None
    id_profesor: Optional[int] = None
    id_periodo: Optional[int] = None
    cupo: Optional[int] = None


class GrupoResponse(BaseModel):
    id_grupo: int
    id_curso: int
    id_profesor: int
    id_periodo: int
    cupo: int

    model_config = ConfigDict(from_attributes=True)
class EstudianteBase(BaseModel):
    nombre: str
    apellido: str
    correo: str


class EstudianteCreate(EstudianteBase):
    id_estudiante: int


class EstudianteUpdate(EstudianteBase):
    pass


class EstudianteResponse(EstudianteBase):
    id_estudiante: int

    class Config:
        from_attributes = True


class ProfesorBase(BaseModel):
    nombre: str
    apellido: str
    correo: str


class ProfesorCreate(ProfesorBase):
    id_profesor: int


class ProfesorUpdate(ProfesorBase):
    pass


class ProfesorResponse(ProfesorBase):
    id_profesor: int

    class Config:
        from_attributes = True


class NotaBase(BaseModel):
    id_estudiante: int
    id_evaluacion: int
    valor: float


class NotaCreate(NotaBase):
    id_nota: int


class NotaUpdate(NotaBase):
    pass


class NotaResponse(NotaBase):
    id_nota: int

    class Config:
        from_attributes = True


class MatriculaCreate(BaseModel):
    id_estudiante: int
    id_curso: Optional[int] = None
    id_grupo: Optional[int] = None
    fecha_matricula: str


class MatriculaUpdate(BaseModel):
    id_estudiante: Optional[int] = None
    id_curso: Optional[int] = None
    id_grupo: Optional[int] = None
    fecha_matricula: Optional[str] = None


class MatriculaResponse(BaseModel):
    id_matricula: int
    id_estudiante: int
    id_curso: Optional[int] = None
    id_grupo: Optional[int] = None
    fecha_matricula: str

    model_config = ConfigDict(from_attributes=True)


class EvaluacionCreate(BaseModel):
    nombre: str
    descripcion: str
    tipo: str
    id_grupo: int
    fecha: str
    valor_maximo: float


class EvaluacionUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    tipo: Optional[str] = None
    id_grupo: Optional[int] = None
    fecha: Optional[str] = None
    valor_maximo: Optional[float] = None


class EvaluacionResponse(BaseModel):
    id_evaluacion: int
    nombre: str
    descripcion: str
    tipo: str
    id_grupo: int
    fecha: str
    valor_maximo: float

    model_config = ConfigDict(from_attributes=True)


class PeriodoAcademicoCreate(BaseModel):
    nombre: str


class PeriodoAcademicoUpdate(BaseModel):
    nombre: Optional[str] = None


class PeriodoAcademicoResponse(BaseModel):
    id_periodo: int
    nombre: str

    model_config = ConfigDict(from_attributes=True)

