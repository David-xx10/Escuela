from typing import List

from fastapi import APIRouter, HTTPException, status

from src.api.schemas import EvaluacionCreate, EvaluacionResponse, EvaluacionUpdate
from src.crud.evaluacion_crud import EvaluacionCRUD
from src.entities.evaluacion import Evaluacion

router = APIRouter(prefix="/evaluaciones", tags=["evaluaciones"])
evaluacion_crud = EvaluacionCRUD()


@router.get(
	"/",
	response_model=List[EvaluacionResponse],
	status_code=status.HTTP_200_OK,
)
def listar_evaluaciones() -> List[EvaluacionResponse]:
	return evaluacion_crud.listar_evaluaciones()


@router.get(
	"/{id_evaluacion}",
	response_model=EvaluacionResponse,
	status_code=status.HTTP_200_OK,
)
def obtener_evaluacion(id_evaluacion: int) -> EvaluacionResponse:
	evaluacion = evaluacion_crud.obtener_evaluacion(id_evaluacion)
	if evaluacion is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Evaluación no encontrada.",
		)
	return evaluacion


@router.post(
	"/",
	response_model=EvaluacionResponse,
	status_code=status.HTTP_201_CREATED,
)
def crear_evaluacion(datos: EvaluacionCreate) -> EvaluacionResponse:
	try:
		return evaluacion_crud.crear_evaluacion(Evaluacion(**datos.model_dump()))
	except ValueError as error:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=str(error),
		) from error


@router.put(
	"/{id_evaluacion}",
	response_model=EvaluacionResponse,
	status_code=status.HTTP_200_OK,
)
def actualizar_evaluacion(
	id_evaluacion: int,
	datos: EvaluacionUpdate,
) -> EvaluacionResponse:
	evaluacion_actual = evaluacion_crud.obtener_evaluacion(id_evaluacion)
	if evaluacion_actual is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Evaluación no encontrada.",
		)

	datos_evaluacion = {
		"id_evaluacion": evaluacion_actual.id_evaluacion,
		"nombre": evaluacion_actual.nombre,
		"descripcion": evaluacion_actual.descripcion,
		"tipo": evaluacion_actual.tipo,
		"id_grupo": evaluacion_actual.id_grupo,
		"fecha": evaluacion_actual.fecha,
		"valor_maximo": evaluacion_actual.valor_maximo,
		**datos.model_dump(exclude_unset=True),
	}
	evaluacion_actualizada = evaluacion_crud.actualizar_evaluacion(
		id_evaluacion,
		Evaluacion(**datos_evaluacion),
	)
	if evaluacion_actualizada is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Evaluación no encontrada.",
		)
	return evaluacion_actualizada


@router.delete(
	"/{id_evaluacion}",
	status_code=status.HTTP_204_NO_CONTENT,
)
def eliminar_evaluacion(id_evaluacion: int) -> None:
	eliminado = evaluacion_crud.eliminar_evaluacion(id_evaluacion)
	if not eliminado:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Evaluación no encontrada.",
		)
