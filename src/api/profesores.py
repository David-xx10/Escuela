from fastapi import APIRouter, HTTPException, status
from src.crud.profesor_crud import ProfesorCRUD
from src.entities.profesor import Profesor
from src.api.schemas import ProfesorCreate, ProfesorUpdate, ProfesorResponse

router = APIRouter(prefix="/profesores", tags=["Profesores"])


@router.get("/", response_model=list[ProfesorResponse], status_code=status.HTTP_200_OK)
def listar_profesores():
    crud = ProfesorCRUD()
    return crud.listar_profesores()


@router.get("/{id_profesor}", response_model=ProfesorResponse, status_code=status.HTTP_200_OK)
def obtener_profesor(id_profesor: int):
    crud = ProfesorCRUD()
    profesor = crud.obtener(id_profesor)
    if profesor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no encontrado")
    return profesor


@router.post("/", response_model=ProfesorResponse, status_code=status.HTTP_201_CREATED)
def crear_profesor(datos: ProfesorCreate):
    crud = ProfesorCRUD()
    nuevo = Profesor(
        id_profesor=datos.id_profesor,
        nombre=datos.nombre,
        apellido=datos.apellido,
        correo=datos.correo,
    )
    return crud.crear(nuevo)


@router.put("/{id_profesor}", response_model=ProfesorResponse, status_code=status.HTTP_200_OK)
def actualizar_profesor(id_profesor: int, datos: ProfesorUpdate):
    crud = ProfesorCRUD()
    actualizado = Profesor(
        id_profesor=id_profesor,
        nombre=datos.nombre,
        apellido=datos.apellido,
        correo=datos.correo,
    )
    resultado = crud.actualizar(id_profesor, actualizado)
    if resultado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no encontrado")
    return resultado


@router.delete("/{id_profesor}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_profesor(id_profesor: int):
    crud = ProfesorCRUD()
    eliminado = crud.eliminar(id_profesor)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no encontrado")