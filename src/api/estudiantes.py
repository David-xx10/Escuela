from fastapi import APIRouter, HTTPException, status
from src.crud.estudiante_crud import EstudianteCRUD
from src.entities.estudiante import Estudiante
from src.api.schemas import EstudianteCreate, EstudianteUpdate, EstudianteResponse

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])


@router.get("/", response_model=list[EstudianteResponse], status_code=status.HTTP_200_OK)
def listar_estudiantes():
    crud = EstudianteCRUD()
    return crud.listar_estudiantes()


@router.get("/{id_estudiante}", response_model=EstudianteResponse, status_code=status.HTTP_200_OK)
def obtener_estudiante(id_estudiante: int):
    crud = EstudianteCRUD()
    estudiante = crud.obtener_estudiante(id_estudiante)
    if estudiante is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estudiante no encontrado")
    return estudiante


@router.post("/", response_model=EstudianteResponse, status_code=status.HTTP_201_CREATED)
def crear_estudiante(datos: EstudianteCreate):
    crud = EstudianteCRUD()
    nuevo = Estudiante(
        id_estudiante=datos.id_estudiante,
        nombre=datos.nombre,
        apellido=datos.apellido,
        correo=datos.correo,
    )
    return crud.crear_estudiante(nuevo)


@router.put("/{id_estudiante}", response_model=EstudianteResponse, status_code=status.HTTP_200_OK)
def actualizar_estudiante(id_estudiante: int, datos: EstudianteUpdate):
    crud = EstudianteCRUD()
    actualizado = Estudiante(
        id_estudiante=id_estudiante,
        nombre=datos.nombre,
        apellido=datos.apellido,
        correo=datos.correo,
    )
    resultado = crud.actualizar_estudiante(id_estudiante, actualizado)
    if resultado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estudiante no encontrado")
    return resultado


@router.delete("/{id_estudiante}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_estudiante(id_estudiante: int):
    crud = EstudianteCRUD()
    eliminado = crud.eliminar_estudiante(id_estudiante)
    if not eliminado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estudiante no encontrado")