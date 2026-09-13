from src.seeders.facultad_seeder import seed_facultades
from src.seeders.curso_seeder import seed_cursos
from src.seeders.periodo_seeder import seed_periodos
from src.seeders.profesor_seeder import seed_profesores
from src.seeders.grupo_seeder import seed_grupos
from src.seeders.matricula_seeder import seed_matriculas
from src.seeders.evaluacion_seeder import seed_evaluaciones


def ejecutar_seeders():
    print("Iniciando la carga de datos iniciales en Neon...")
    seed_facultades()
    seed_cursos()
    seed_profesores()
    seed_periodos()
    seed_grupos()
    seed_matriculas()
    seed_evaluaciones()
    print(" Carga inicial de datos completada exitosamente.")


if __name__ == "__main__":
    ejecutar_seeders()
