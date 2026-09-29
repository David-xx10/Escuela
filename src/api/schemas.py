from typing import Optional

from pydantic import BaseModel, ConfigDict


class FacultadBase(BaseModel):
    id_facultad: int
    nombre: str


class FacultadCreate(FacultadBase):
    pass


class FacultadUpdate(BaseModel):
    id_facultad: Optional[int] = None
    nombre: Optional[str] = None


class FacultadResponse(FacultadBase):
    model_config = ConfigDict(from_attributes=True)


class CursoBase(BaseModel):
    id_curso: int
    nombre: str
    creditos: int
    id_facultad: int


class CursoCreate(CursoBase):
    pass


class CursoUpdate(BaseModel):
    id_curso: Optional[int] = None
    nombre: Optional[str] = None
    creditos: Optional[int] = None
    id_facultad: Optional[int] = None


class CursoResponse(CursoBase):
    model_config = ConfigDict(from_attributes=True)


class GrupoBase(BaseModel):
    id_grupo: int
    id_curso: int
    id_profesor: int
    id_periodo: int
    cupo: int


class GrupoCreate(GrupoBase):
    pass


class GrupoUpdate(BaseModel):
    id_grupo: Optional[int] = None
    id_curso: Optional[int] = None
    id_profesor: Optional[int] = None
    id_periodo: Optional[int] = None
    cupo: Optional[int] = None


class GrupoResponse(GrupoBase):
    model_config = ConfigDict(from_attributes=True)
