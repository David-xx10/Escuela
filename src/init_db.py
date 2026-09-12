from src.database.conection import Base, engine

# Importas entidades
from src.entities.facultad import Facultad
from src.entities.curso import Curso
from src.entities.grupo import Grupo
from src.entities.periodo_academico import PeriodoAcademico
from src.entities.profesor import Profesor

print("Conectando a Neon y creando tablas...")
Base.metadata.create_all(bind=engine)
print("¡Tablas creadas exitosamente!")
