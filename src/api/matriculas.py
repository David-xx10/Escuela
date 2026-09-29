from typing import List

from fastapi import APIRouter, HTTPException, status

from src.api.schemas import MatriculaCreate, MatriculaResponse, MatriculaUpdate
from src.crud.matricula_crud import MatriculaCRUD
from src.entities.matricula import Matricula

router = APIRouter(prefix="/matriculas", tags=["matriculas"])
matricula_crud = MatriculaCRUD()


@router.get("/", response_model=List[MatriculaResponse], status_code=status.HTTP_200_OK)
def listar_matriculas() -> List[MatriculaResponse]:
	return matricula_crud.listar_matriculas()


@router.get(
	"/{id_matricula}",
	response_model=MatriculaResponse,
	status_code=status.HTTP_200_OK,
)
def obtener_matricula(id_matricula: int) -> MatriculaResponse:
	matricula = matricula_crud.obtener_matricula(id_matricula)
	if matricula is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Matrícula no encontrada.",
		)
	return matricula


@router.post(
	"/",
	response_model=MatriculaResponse,
	status_code=status.HTTP_201_CREATED,
)
def crear_matricula(datos: MatriculaCreate) -> MatriculaResponse:
	try:
		return matricula_crud.crear_matricula(Matricula(**datos.model_dump()))
	except ValueError as error:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=str(error),
		) from error


@router.put(
	"/{id_matricula}",
	response_model=MatriculaResponse,
	status_code=status.HTTP_200_OK,
)
def actualizar_matricula(
	id_matricula: int,
	datos: MatriculaUpdate,
) -> MatriculaResponse:
	matricula_actual = matricula_crud.obtener_matricula(id_matricula)
	if matricula_actual is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Matrícula no encontrada.",
		)

	datos_matricula = {
		"id_matricula": matricula_actual.id_matricula,
		"id_estudiante": matricula_actual.id_estudiante,
		"id_curso": matricula_actual.id_curso,
		"id_grupo": matricula_actual.id_grupo,
		"fecha_matricula": matricula_actual.fecha_matricula,
		**datos.model_dump(exclude_unset=True),
	}
	matricula_actualizada = matricula_crud.actualizar_matricula(
		id_matricula,
		Matricula(**datos_matricula),
	)
	if matricula_actualizada is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Matrícula no encontrada.",
		)
	return matricula_actualizada


@router.delete(
	"/{id_matricula}",
	status_code=status.HTTP_204_NO_CONTENT,
)
def eliminar_matricula(id_matricula: int) -> None:
	eliminado = matricula_crud.eliminar_matricula(id_matricula)
	if not eliminado:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Matrícula no encontrada.",
		)
