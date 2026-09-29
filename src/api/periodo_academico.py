from typing import List

from fastapi import APIRouter, HTTPException, status

from src.api.schemas import (
	PeriodoAcademicoCreate,
	PeriodoAcademicoResponse,
	PeriodoAcademicoUpdate,
)
from src.crud.periodo_academico_crud import PeriodoAcademicoCRUD
from src.entities.periodo_academico import PeriodoAcademico


router = APIRouter(
	prefix="/periodos-academicos",
	tags=["periodos-academicos"],
)
periodo_academico_crud = PeriodoAcademicoCRUD()


@router.get(
	"/",
	response_model=List[PeriodoAcademicoResponse],
	status_code=status.HTTP_200_OK,
)
def listar_periodos_academicos() -> List[PeriodoAcademicoResponse]:
	return periodo_academico_crud.listar_periodos_academicos()


@router.get(
	"/{id_periodo}",
	response_model=PeriodoAcademicoResponse,
	status_code=status.HTTP_200_OK,
)
def obtener_periodo_academico(id_periodo: int) -> PeriodoAcademicoResponse:
	periodo = periodo_academico_crud.obtener_periodo_academico(id_periodo)
	if periodo is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Periodo académico no encontrado.",
		)
	return periodo


@router.post(
	"/",
	response_model=PeriodoAcademicoResponse,
	status_code=status.HTTP_201_CREATED,
)
def crear_periodo_academico(
	datos: PeriodoAcademicoCreate,
) -> PeriodoAcademicoResponse:
	try:
		periodo = PeriodoAcademico(**datos.model_dump())
		return periodo_academico_crud.crear_periodo_academico(periodo)
	except ValueError as error:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=str(error),
		) from error


@router.put(
	"/{id_periodo}",
	response_model=PeriodoAcademicoResponse,
	status_code=status.HTTP_200_OK,
)
def actualizar_periodo_academico(
	id_periodo: int,
	datos: PeriodoAcademicoUpdate,
) -> PeriodoAcademicoResponse:
	periodo_actual = periodo_academico_crud.obtener_periodo_academico(id_periodo)
	if periodo_actual is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Periodo académico no encontrado.",
		)

	datos_periodo = {
		"id_periodo": periodo_actual.id_periodo,
		"nombre": periodo_actual.nombre,
		**datos.model_dump(exclude_unset=True),
	}
	periodo_actualizado = periodo_academico_crud.actualizar_periodo_academico(
		id_periodo,
		PeriodoAcademico(**datos_periodo),
	)
	if periodo_actualizado is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Periodo académico no encontrado.",
		)
	return periodo_actualizado


@router.delete(
	"/{id_periodo}",
	status_code=status.HTTP_204_NO_CONTENT,
)
def eliminar_periodo_academico(id_periodo: int) -> None:
	eliminado = periodo_academico_crud.eliminar_periodo_academico(id_periodo)
	if not eliminado:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Periodo académico no encontrado.",
		)
