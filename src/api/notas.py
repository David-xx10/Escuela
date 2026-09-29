from fastapi import APIRouter, HTTPException, status
from src.crud.nota_crud import NotaCRUD
from src.entities.nota import Nota
from src.api.schemas import NotaCreate, NotaUpdate, NotaResponse

router = APIRouter(prefix="/notas", tags=["Notas"])


@router.get("/", response_model=list[NotaResponse], status_code=status.HTTP_200_OK)
def listar_notas():
    crud = NotaCRUD()
    return crud.listar_notas()


@router.get("/{id_nota}", response_model=NotaResponse, status_code=status.HTTP_200_OK)
def obtener_nota(id_nota: int):
    crud = NotaCRUD()
    nota = crud.obtener_nota(id_nota)
    if nota is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nota no encontrada")
    return nota


@router.post("/", response_model=NotaResponse, status_code=status.HTTP_201_CREATED)
def crear_nota(datos: NotaCreate):
    crud = NotaCRUD()
    nueva = Nota(
        id_nota=datos.id_nota,
        id_estudiante=datos.id_estudiante,
        id_evaluacion=datos.id_evaluacion,
        valor=datos.valor,
    )
    return crud.registrar_nota(nueva)


@router.put("/{id_nota}", response_model=NotaResponse, status_code=status.HTTP_200_OK)
def actualizar_nota(id_nota: int, datos: NotaUpdate):
    crud = NotaCRUD()
    actualizada = Nota(
        id_nota=id_nota,
        id_estudiante=datos.id_estudiante,
        id_evaluacion=datos.id_evaluacion,
        valor=datos.valor,
    )
    resultado = crud.actualizar_nota(id_nota, actualizada)
    if resultado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nota no encontrada")
    return resultado


@router.delete("/{id_nota}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_nota(id_nota: int):
    crud = NotaCRUD()
    eliminada = crud.eliminar_nota(id_nota)
    if not eliminada:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nota no encontrada")