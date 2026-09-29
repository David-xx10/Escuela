from typing import List

from fastapi import APIRouter, HTTPException, status

from src.api.schemas import (
    FacultadCreate,
    FacultadResponse,
    FacultadUpdate,
)
from src.crud.facultad_crud import FacultadCRUD
from src.entities.facultad import Facultad


router = APIRouter(prefix="/facultades", tags=["facultades"])
facultad_crud = FacultadCRUD()


@router.get("/", response_model=List[FacultadResponse], status_code=status.HTTP_200_OK)
def listar_facultades() -> List[FacultadResponse]:
    return facultad_crud.listar_facultades()


@router.get(
    "/{id_facultad}",
    response_model=FacultadResponse,
    status_code=status.HTTP_200_OK,
)
def obtener_facultad(id_facultad: int) -> FacultadResponse:
    facultad = facultad_crud.obtener_facultad(id_facultad)
    if facultad is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Facultad no encontrada.",
        )
    return facultad


@router.post(
    "/",
    response_model=FacultadResponse,
    status_code=status.HTTP_201_CREATED,
)
def crear_facultad(datos: FacultadCreate) -> FacultadResponse:
    try:
        return facultad_crud.crear_facultad(Facultad(**datos.model_dump()))
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error


@router.put(
    "/{id_facultad}",
    response_model=FacultadResponse,
    status_code=status.HTTP_200_OK,
)
def actualizar_facultad(
    id_facultad: int, datos: FacultadUpdate
) -> FacultadResponse:
    facultad_actual = facultad_crud.obtener_facultad(id_facultad)
    if facultad_actual is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Facultad no encontrada.",
        )

    datos_facultad = {
        "id_facultad": facultad_actual.id_facultad,
        "nombre": facultad_actual.nombre,
        **datos.model_dump(exclude_unset=True),
    }
    facultad_actualizada = facultad_crud.actualizar_facultad(
        id_facultad,
        Facultad(**datos_facultad),
    )
    if facultad_actualizada is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Facultad no encontrada.",
        )
    return facultad_actualizada


@router.delete(
    "/{id_facultad}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def eliminar_facultad(id_facultad: int) -> None:
    eliminado = facultad_crud.eliminar_facultad(id_facultad)
    if not eliminado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Facultad no encontrada.",
        )
