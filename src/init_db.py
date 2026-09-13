from src.database.conection import Base, engine

# Importas entidades
from src.entities.facultad import Facultad
from src.entities.curso import Curso
from src.entities.grupo import Grupo
from src.entities.periodo_academico import PeriodoAcademico
from src.entities.profesor import Profesor
from src.entities.estudiante import Estudiante
from src.entities.nota import Nota
from src.entities.evaluacion import Evaluacion
from src.entities.matricula import Matricula
from src.entities.persona import Persona

print("Conectando a Neon y creando tablas...")
Base.metadata.create_all(bind=engine)
print("¡Tablas creadas exitosamente!")
