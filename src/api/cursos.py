from typing import List

from fastapi import APIRouter, HTTPException, status

from src.api.schemas import CursoCreate, CursoResponse, CursoUpdate
from src.crud.curso_crud import CursoCRUD
from src.entities.curso import Curso

router = APIRouter(prefix="/cursos", tags=["cursos"])
curso_crud = CursoCRUD()


@router.get("/", response_model=List[CursoResponse], status_code=status.HTTP_200_OK)
def listar_cursos() -> List[CursoResponse]:
    return curso_crud.listar_cursos()


@router.get(
    "/{id_curso}",
    response_model=CursoResponse,
    status_code=status.HTTP_200_OK,
)
def obtener_curso(id_curso: int) -> CursoResponse:
    curso = curso_crud.obtener_curso(id_curso)
    if curso is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso no encontrado.",
        )
    return curso


@router.post(
    "/",
    response_model=CursoResponse,
    status_code=status.HTTP_201_CREATED,
)
def crear_curso(datos: CursoCreate) -> CursoResponse:
    try:
        return curso_crud.crear_curso(Curso(**datos.model_dump()))
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error


@router.put(
    "/{id_curso}",
    response_model=CursoResponse,
    status_code=status.HTTP_200_OK,
)
def actualizar_curso(id_curso: int, datos: CursoUpdate) -> CursoResponse:
    curso_actual = curso_crud.obtener_curso(id_curso)
    if curso_actual is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso no encontrado.",
        )

    datos_curso = {
        "id_curso": curso_actual.id_curso,
        "nombre": curso_actual.nombre,
        "creditos": curso_actual.creditos,
        "id_facultad": curso_actual.id_facultad,
        **datos.model_dump(exclude_unset=True),
    }
    curso_actualizado = curso_crud.actualizar_curso(
        id_curso,
        Curso(**datos_curso),
    )
    if curso_actualizado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso no encontrado.",
        )
    return curso_actualizado


@router.delete(
    "/{id_curso}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def eliminar_curso(id_curso: int) -> None:
    eliminado = curso_crud.eliminar_curso(id_curso)
    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Curso no encontrado.",
        )
