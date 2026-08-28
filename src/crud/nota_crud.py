from src.entities.nota import Nota

notas: list[Nota] = []

def registrar_nota(id_nota: int, id_estudiante: int, id_evaluacion: int, valor: float) -> Nota:
    nueva_nota = Nota(id_nota, id_estudiante, id_evaluacion, valor)
    notas.append(nueva_nota)
    return nueva_nota

def listar_notas() -> list[Nota]:
    return notas

def calcular_promedio(id_estudiante: int) -> float:
    notas_estudiante = [n.valor for n in notas if n.id_estudiante == id_estudiante]
    if not notas_estudiante:
        return 0.0
    return sum(notas_estudiante) / len(notas_estudiante)