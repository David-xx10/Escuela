from typing import List

from fastapi import APIRouter, HTTPException, status

from src.api.schemas import GrupoCreate, GrupoResponse, GrupoUpdate
from src.crud.grupo_crud import GrupoCRUD
from src.entities.grupo import Grupo


router = APIRouter(prefix="/grupos", tags=["grupos"])
grupo_crud = GrupoCRUD()


@router.get("/", response_model=List[GrupoResponse], status_code=status.HTTP_200_OK)
def listar_grupos() -> List[GrupoResponse]:
    return grupo_crud.listar_grupos()


@router.get(
    "/{id_grupo}",
    response_model=GrupoResponse,
    status_code=status.HTTP_200_OK,
)
def obtener_grupo(id_grupo: int) -> GrupoResponse:
    grupo = grupo_crud.obtener_grupo(id_grupo)
    if grupo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Grupo no encontrado.",
        )
    return grupo


@router.post(
    "/",
    response_model=GrupoResponse,
    status_code=status.HTTP_201_CREATED,
)
def crear_grupo(datos: GrupoCreate) -> GrupoResponse:
    try:
        return grupo_crud.crear_grupo(Grupo(**datos.model_dump()))
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error


@router.put(
    "/{id_grupo}",
    response_model=GrupoResponse,
    status_code=status.HTTP_200_OK,
)
def actualizar_grupo(id_grupo: int, datos: GrupoUpdate) -> GrupoResponse:
    grupo_actual = grupo_crud.obtener_grupo(id_grupo)
    if grupo_actual is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Grupo no encontrado.",
        )

    datos_grupo = {
        "id_grupo": grupo_actual.id_grupo,
        "id_curso": grupo_actual.id_curso,
        "id_profesor": grupo_actual.id_profesor,
        "id_periodo": grupo_actual.id_periodo,
        "cupo": grupo_actual.cupo,
        **datos.model_dump(exclude_unset=True),
    }
    grupo_actualizado = grupo_crud.actualizar_grupo(
        id_grupo,
        Grupo(**datos_grupo),
    )
    if grupo_actualizado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Grupo no encontrado.",
        )
    return grupo_actualizado


@router.delete(
    "/{id_grupo}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def eliminar_grupo(id_grupo: int) -> None:
    eliminado = grupo_crud.eliminar_grupo(id_grupo)
    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Grupo no encontrado.",
        )
