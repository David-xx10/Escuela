from src.crud.estudiante_crud import EstudianteCRUD
from src.crud.profesor_crud import ProfesorCRUD
from src.crud.curso_crud import CursoCRUD
from src.crud.facultad_crud import FacultadCRUD
from src.crud.grupo_crud import GrupoCRUD
from src.crud.matricula_crud import MatriculaCRUD
from src.crud.nota_crud import NotaCRUD
from src.crud.evaluacion_crud import EvaluacionCRUD
from src.crud.periodo_academico_crud import (
    crear_periodo_academico,
    obtener_periodo_academico,
    actualizar_periodo_academico,
    eliminar_periodo_academico,
    listar_periodos_academicos,
)

from src.entities.estudiante import Estudiante
from src.entities.profesor import Profesor
from src.entities.curso import Curso
from src.entities.facultad import Facultad
from src.entities.grupo import Grupo
from src.entities.matricula import Matricula
from src.entities.nota import Nota
from src.entities.evaluacion import Evaluacion


# Instancias globales de CRUD
estudiante_crud = EstudianteCRUD()
profesor_crud = ProfesorCRUD()
curso_crud = CursoCRUD()
facultad_crud = FacultadCRUD()
grupo_crud = GrupoCRUD()
matricula_crud = MatriculaCRUD()
nota_crud = NotaCRUD()
evaluacion_crud = EvaluacionCRUD()


def mostrar_menu_principal():
    print("\n" + "=" * 50)
    print("SISTEMA DE GESTIÓN ACADÉMICA")
    print("=" * 50)
    print("1. Gestionar Estudiantes")
    print("2. Gestionar Profesores")
    print("3. Gestionar Facultades")
    print("4. Gestionar Cursos")
    print("5. Gestionar Grupos")
    print("6. Gestionar Evaluaciones")
    print("7. Gestionar Períodos Académicos")
    print("8. Gestionar Matrículas")
    print("9. Registrar Notas")
    print("10. Ver Promedio Estudiante")
    print("11. Listar Estudiantes")
    print("0. Salir")
    print("=" * 50)


def menu_estudiantes():
    while True:
        print("\n--- ESTUDIANTES ---")
        print("1. Crear Estudiante")
        print("2. Obtener Estudiante")
        print("3. Actualizar Estudiante")
        print("4. Eliminar Estudiante")
        print("5. Listar Estudiantes")
        print("0. Volver")

        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            try:
                id_persona = int(input("ID Persona: "))
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                correo = input("Correo: ")
                id_estudiante = int(input("ID Estudiante: "))
                
                estudiante = Estudiante(id_persona, nombre, apellido, correo, id_estudiante)
                estudiante_crud.crear_estudiante(estudiante)
                print(f"✓ Estudiante creado: {estudiante}")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "2":
            try:
                id_estudiante = int(input("ID Estudiante: "))
                estudiante = estudiante_crud.obtener_estudiante(id_estudiante)
                if estudiante:
                    print(f"✓ {estudiante}")
                else:
                    print("✗ Estudiante no encontrado")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "3":
            try:
                id_estudiante = int(input("ID Estudiante a actualizar: "))
                id_persona = int(input("Nuevo ID Persona: "))
                nombre = input("Nuevo Nombre: ")
                apellido = input("Nuevo Apellido: ")
                correo = input("Nuevo Correo: ")
                
                estudiante = Estudiante(id_persona, nombre, apellido, correo, id_estudiante)
                actualizado = estudiante_crud.actualizar_estudiante(id_estudiante, estudiante)
                if actualizado:
                    print(f"✓ Estudiante actualizado: {actualizado}")
                else:
                    print("✗ Estudiante no encontrado")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "4":
            try:
                id_estudiante = int(input("ID Estudiante a eliminar: "))
                if estudiante_crud.eliminar_estudiante(id_estudiante):
                    print("✓ Estudiante eliminado")
                else:
                    print("✗ Estudiante no encontrado")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "5":
            estudiantes = estudiante_crud.listar_estudiantes()
            if estudiantes:
                print("\n--- Lista de Estudiantes ---")
                for est in estudiantes:
                    print(f"  {est}")
            else:
                print("No hay estudiantes registrados")

        elif opcion == "0":
            break


def menu_profesores():
    while True:
        print("\n--- PROFESORES ---")
        print("1. Crear Profesor")
        print("2. Obtener Profesor")
        print("3. Actualizar Profesor")
        print("4. Eliminar Profesor")
        print("5. Listar Profesores")
        print("0. Volver")

        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            try:
                id_persona = int(input("ID Persona: "))
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                correo = input("Correo: ")
                id_profesor = int(input("ID Profesor: "))
                
                profesor = Profesor(id_persona, nombre, apellido, correo, id_profesor)
                profesor_crud.crear(profesor)
                print(f"✓ Profesor creado: {profesor}")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "2":
            try:
                id_profesor = int(input("ID Profesor: "))
                profesor = profesor_crud.obtener(id_profesor)
                if profesor:
                    print(f"✓ {profesor}")
                else:
                    print("✗ Profesor no encontrado")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "3":
            try:
                id_profesor = int(input("ID Profesor a actualizar: "))
                id_persona = int(input("Nuevo ID Persona: "))
                nombre = input("Nuevo Nombre: ")
                apellido = input("Nuevo Apellido: ")
                correo = input("Nuevo Correo: ")
                
                profesor = Profesor(id_persona, nombre, apellido, correo, id_profesor)
                actualizado = profesor_crud.actualizar(id_profesor, profesor)
                if actualizado:
                    print(f"✓ Profesor actualizado: {actualizado}")
                else:
                    print("✗ Profesor no encontrado")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "4":
            try:
                id_profesor = int(input("ID Profesor a eliminar: "))
                if profesor_crud.eliminar(id_profesor):
                    print("✓ Profesor eliminado")
                else:
                    print("✗ Profesor no encontrado")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "5":
            profesores = profesor_crud.listar_profesores()
            if profesores:
                print("\n--- Lista de Profesores ---")
                for prof in profesores:
                    print(f"  {prof}")
            else:
                print("No hay profesores registrados")

        elif opcion == "0":
            break


def menu_facultades():
    while True:
        print("\n--- FACULTADES ---")
        print("1. Crear Facultad")
        print("2. Obtener Facultad")
        print("3. Actualizar Facultad")
        print("4. Eliminar Facultad")
        print("5. Listar Facultades")
        print("0. Volver")

        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            try:
                id_facultad = int(input("ID Facultad: "))
                nombre = input("Nombre: ")
                
                facultad = Facultad(id_facultad, nombre)
                facultad_crud.crear_facultad(facultad)
                print(f"✓ Facultad creada: {facultad}")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "2":
            try:
                id_facultad = int(input("ID Facultad: "))
                facultad = facultad_crud.obtener_facultad(id_facultad)
                if facultad:
                    print(f"✓ {facultad}")
                else:
                    print("✗ Facultad no encontrada")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "3":
            try:
                id_facultad = int(input("ID Facultad a actualizar: "))
                nombre = input("Nuevo Nombre: ")
                
                facultad = Facultad(id_facultad, nombre)
                actualizada = facultad_crud.actualizar_facultad(id_facultad, facultad)
                if actualizada:
                    print(f"✓ Facultad actualizada: {actualizada}")
                else:
                    print("✗ Facultad no encontrada")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "4":
            try:
                id_facultad = int(input("ID Facultad a eliminar: "))
                if facultad_crud.eliminar_facultad(id_facultad):
                    print("✓ Facultad eliminada")
                else:
                    print("✗ Facultad no encontrada")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "5":
            facultades = facultad_crud.listar_facultades()
            if facultades:
                print("\n--- Lista de Facultades ---")
                for fac in facultades:
                    print(f"  {fac}")
            else:
                print("No hay facultades registradas")

        elif opcion == "0":
            break


def menu_cursos():
    while True:
        print("\n--- CURSOS ---")
        print("1. Crear Curso")
        print("2. Obtener Curso")
        print("3. Actualizar Curso")
        print("4. Eliminar Curso")
        print("5. Listar Cursos")
        print("0. Volver")

        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            try:
                id_curso = int(input("ID Curso: "))
                nombre = input("Nombre: ")
                creditos = int(input("Créditos: "))
                id_facultad = int(input("ID Facultad: "))
                
                curso = Curso(id_curso, nombre, creditos, id_facultad)
                curso_crud.crear_curso(curso)
                print(f"✓ Curso creado: {curso}")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "2":
            try:
                id_curso = int(input("ID Curso: "))
                curso = curso_crud.obtener_curso(id_curso)
                if curso:
                    print(f"✓ {curso}")
                else:
                    print("✗ Curso no encontrado")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "3":
            try:
                id_curso = int(input("ID Curso a actualizar: "))
                nombre = input("Nuevo Nombre: ")
                creditos = int(input("Nuevos Créditos: "))
                id_facultad = int(input("Nuevo ID Facultad: "))
                
                curso = Curso(id_curso, nombre, creditos, id_facultad)
                actualizado = curso_crud.actualizar_curso(id_curso, curso)
                if actualizado:
                    print(f"✓ Curso actualizado: {actualizado}")
                else:
                    print("✗ Curso no encontrado")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "4":
            try:
                id_curso = int(input("ID Curso a eliminar: "))
                if curso_crud.eliminar_curso(id_curso):
                    print("✓ Curso eliminado")
                else:
                    print("✗ Curso no encontrado")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "5":
            cursos = curso_crud.listar_cursos()
            if cursos:
                print("\n--- Lista de Cursos ---")
                for cur in cursos:
                    print(f"  {cur}")
            else:
                print("No hay cursos registrados")

        elif opcion == "0":
            break


def menu_grupos():
    while True:
        print("\n--- GRUPOS ---")
        print("1. Crear Grupo")
        print("2. Obtener Grupo")
        print("3. Actualizar Grupo")
        print("4. Eliminar Grupo")
        print("5. Listar Grupos")
        print("0. Volver")

        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            try:
                id_grupo = int(input("ID Grupo: "))
                id_curso = int(input("ID Curso: "))
                id_profesor = int(input("ID Profesor: "))
                cupo = int(input("Cupo: "))
                
                grupo = Grupo(id_grupo, id_curso, id_profesor, cupo)
                grupo_crud.crear_grupo(grupo)
                print(f"✓ Grupo creado: {grupo}")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "2":
            try:
                id_grupo = int(input("ID Grupo: "))
                grupo = grupo_crud.obtener_grupo(id_grupo)
                if grupo:
                    print(f"✓ {grupo}")
                else:
                    print("✗ Grupo no encontrado")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "3":
            try:
                id_grupo = int(input("ID Grupo a actualizar: "))
                id_curso = int(input("Nuevo ID Curso: "))
                id_profesor = int(input("Nuevo ID Profesor: "))
                cupo = int(input("Nuevo Cupo: "))
                
                grupo = Grupo(id_grupo, id_curso, id_profesor, cupo)
                actualizado = grupo_crud.actualizar_grupo(id_grupo, grupo)
                if actualizado:
                    print(f"✓ Grupo actualizado: {actualizado}")
                else:
                    print("✗ Grupo no encontrado")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "4":
            try:
                id_grupo = int(input("ID Grupo a eliminar: "))
                if grupo_crud.eliminar_grupo(id_grupo):
                    print("✓ Grupo eliminado")
                else:
                    print("✗ Grupo no encontrado")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "5":
            grupos = grupo_crud.listar_grupos()
            if grupos:
                print("\n--- Lista de Grupos ---")
                for grp in grupos:
                    print(f"  {grp}")
            else:
                print("No hay grupos registrados")

        elif opcion == "0":
            break


def menu_evaluaciones():
    while True:
        print("\n--- EVALUACIONES ---")
        print("1. Crear Evaluación")
        print("2. Obtener Evaluación")
        print("3. Actualizar Evaluación")
        print("4. Eliminar Evaluación")
        print("5. Listar Evaluaciones")
        print("0. Volver")

        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            try:
                id_evaluacion = int(input("ID Evaluación: "))
                nombre = input("Nombre: ")
                descripcion = input("Descripción: ")
                tipo = input("Tipo (Quiz/Examen/Taller): ")
                id_grupo = int(input("ID Grupo: "))
                fecha = input("Fecha (YYYY-MM-DD): ")
                valor_maximo = float(input("Valor Máximo: "))
                
                evaluacion = Evaluacion(id_evaluacion, nombre, descripcion, tipo, id_grupo, fecha, valor_maximo)
                evaluacion_crud.crear_evaluacion(evaluacion)
                print(f"✓ Evaluación creada: {evaluacion}")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "2":
            try:
                id_evaluacion = int(input("ID Evaluación: "))
                evaluacion = evaluacion_crud.obtener_evaluacion(id_evaluacion)
                if evaluacion:
                    print(f"✓ {evaluacion}")
                else:
                    print("✗ Evaluación no encontrada")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "3":
            try:
                id_evaluacion = int(input("ID Evaluación a actualizar: "))
                nombre = input("Nuevo Nombre: ")
                descripcion = input("Nueva Descripción: ")
                tipo = input("Nuevo Tipo: ")
                id_grupo = int(input("Nuevo ID Grupo: "))
                fecha = input("Nueva Fecha: ")
                valor_maximo = float(input("Nuevo Valor Máximo: "))
                
                evaluacion = Evaluacion(id_evaluacion, nombre, descripcion, tipo, id_grupo, fecha, valor_maximo)
                actualizada = evaluacion_crud.actualizar_evaluacion(id_evaluacion, evaluacion)
                if actualizada:
                    print(f"✓ Evaluación actualizada: {actualizada}")
                else:
                    print("✗ Evaluación no encontrada")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "4":
            try:
                id_evaluacion = int(input("ID Evaluación a eliminar: "))
                if evaluacion_crud.eliminar_evaluacion(id_evaluacion):
                    print("✓ Evaluación eliminada")
                else:
                    print("✗ Evaluación no encontrada")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "5":
            evaluaciones = evaluacion_crud.listar_evaluaciones()
            if evaluaciones:
                print("\n--- Lista de Evaluaciones ---")
                for eva in evaluaciones:
                    print(f"  {eva}")
            else:
                print("No hay evaluaciones registradas")

        elif opcion == "0":
            break


def menu_periodos():
    while True:
        print("\n--- PERÍODOS ACADÉMICOS ---")
        print("1. Crear Período")
        print("2. Obtener Período")
        print("3. Actualizar Período")
        print("4. Eliminar Período")
        print("5. Listar Períodos")
        print("0. Volver")

        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            try:
                id_periodo = int(input("ID Período: "))
                nombre = input("Nombre: ")
                fecha_inicio = input("Fecha Inicio (YYYY-MM-DD): ")
                fecha_fin = input("Fecha Fin (YYYY-MM-DD): ")
                
                crear_periodo_academico(id_periodo, nombre, fecha_inicio, fecha_fin)
                print(f"✓ Período creado")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "2":
            try:
                id_periodo = int(input("ID Período: "))
                periodo = obtener_periodo_academico(id_periodo)
                if periodo:
                    print(f"✓ {periodo}")
                else:
                    print("✗ Período no encontrado")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "3":
            try:
                id_periodo = int(input("ID Período a actualizar: "))
                nombre = input("Nuevo Nombre: ")
                fecha_inicio = input("Nueva Fecha Inicio: ")
                fecha_fin = input("Nueva Fecha Fin: ")
                
                actualizado = actualizar_periodo_academico(id_periodo, nombre=nombre, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
                if actualizado:
                    print(f"✓ Período actualizado: {actualizado}")
                else:
                    print("✗ Período no encontrado")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "4":
            try:
                id_periodo = int(input("ID Período a eliminar: "))
                eliminado = eliminar_periodo_academico(id_periodo)
                if eliminado:
                    print("✓ Período eliminado")
                else:
                    print("✗ Período no encontrado")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "5":
            periodos = listar_periodos_academicos()
            if periodos:
                print("\n--- Lista de Períodos Académicos ---")
                for per in periodos:
                    print(f"  {per}")
            else:
                print("No hay períodos registrados")

        elif opcion == "0":
            break


def menu_matriculas():
    while True:
        print("\n--- MATRÍCULAS ---")
        print("1. Crear Matrícula")
        print("2. Obtener Matrícula")
        print("3. Actualizar Matrícula")
        print("4. Eliminar Matrícula")
        print("5. Listar Matrículas")
        print("0. Volver")

        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            try:
                id_matricula = int(input("ID Matrícula: "))
                id_estudiante = int(input("ID Estudiante: "))
                id_grupo = int(input("ID Grupo: "))
                fecha_matricula = input("Fecha Matrícula (YYYY-MM-DD): ")
                
                matricula = Matricula(id_matricula, id_estudiante, id_grupo, fecha_matricula)
                matricula_crud.crear_matricula(matricula)
                print(f"✓ Matrícula creada: {matricula}")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "2":
            try:
                id_matricula = int(input("ID Matrícula: "))
                matricula = matricula_crud.obtener_matricula(id_matricula)
                if matricula:
                    print(f"✓ {matricula}")
                else:
                    print("✗ Matrícula no encontrada")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "3":
            try:
                id_matricula = int(input("ID Matrícula a actualizar: "))
                id_estudiante = int(input("Nuevo ID Estudiante: "))
                id_grupo = int(input("Nuevo ID Grupo: "))
                fecha_matricula = input("Nueva Fecha Matrícula: ")
                
                matricula = Matricula(id_matricula, id_estudiante, id_grupo, fecha_matricula)
                actualizada = matricula_crud.actualizar_matricula(id_matricula, matricula)
                if actualizada:
                    print(f"✓ Matrícula actualizada: {actualizada}")
                else:
                    print("✗ Matrícula no encontrada")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "4":
            try:
                id_matricula = int(input("ID Matrícula a eliminar: "))
                if matricula_crud.eliminar_matricula(id_matricula):
                    print("✓ Matrícula eliminada")
                else:
                    print("✗ Matrícula no encontrada")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "5":
            matriculas = matricula_crud.listar_matriculas()
            if matriculas:
                print("\n--- Lista de Matrículas ---")
                for mat in matriculas:
                    print(f"  {mat}")
            else:
                print("No hay matrículas registradas")

        elif opcion == "0":
            break


def menu_notas():
    while True:
        print("\n--- NOTAS ---")
        print("1. Registrar Nota")
        print("2. Obtener Nota")
        print("3. Actualizar Nota")
        print("4. Eliminar Nota")
        print("5. Listar Notas")
        print("0. Volver")

        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            try:
                id_nota = int(input("ID Nota: "))
                id_estudiante = int(input("ID Estudiante: "))
                id_evaluacion = int(input("ID Evaluación: "))
                valor = float(input("Valor Nota: "))
                
                nota = Nota(id_nota, id_estudiante, id_evaluacion, valor)
                nota_crud.registrar_nota(nota)
                print(f"✓ Nota registrada: {nota}")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "2":
            try:
                id_nota = int(input("ID Nota: "))
                nota = nota_crud.obtener_nota(id_nota)
                if nota:
                    print(f"✓ {nota}")
                else:
                    print("✗ Nota no encontrada")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "3":
            try:
                id_nota = int(input("ID Nota a actualizar: "))
                id_estudiante = int(input("Nuevo ID Estudiante: "))
                id_evaluacion = int(input("Nuevo ID Evaluación: "))
                valor = float(input("Nuevo Valor: "))
                
                nota = Nota(id_nota, id_estudiante, id_evaluacion, valor)
                actualizada = nota_crud.actualizar_nota(id_nota, nota)
                if actualizada:
                    print(f"✓ Nota actualizada: {actualizada}")
                else:
                    print("✗ Nota no encontrada")
            except ValueError as e:
                print(f"✗ Error: {e}")

        elif opcion == "4":
            try:
                id_nota = int(input("ID Nota a eliminar: "))
                if nota_crud.eliminar_nota(id_nota):
                    print("✓ Nota eliminada")
                else:
                    print("✗ Nota no encontrada")
            except ValueError:
                print("✗ ID inválido")

        elif opcion == "5":
            notas = nota_crud.listar_notas()
            if notas:
                print("\n--- Lista de Notas ---")
                for nota in notas:
                    print(f"  {nota}")
            else:
                print("No hay notas registradas")

        elif opcion == "0":
            break


def ver_promedio_estudiante():
    try:
        id_estudiante = int(input("ID Estudiante: "))
        promedio = nota_crud.calcular_promedio(id_estudiante)
        print(f"✓ Promedio del estudiante {id_estudiante}: {promedio:.2f}")
    except ValueError:
        print("✗ ID inválido")


def listar_estudiantes_relaciones():
    estudiantes = estudiante_crud.listar_estudiantes()
    if not estudiantes:
        print("No hay estudiantes registrados")
        return
    
    print("\n--- ESTUDIANTES REGISTRADOS ---")
    for est in estudiantes:
        print(f"\n{est}")
        
        # Mostrar matrículas del estudiante
        matriculas = [m for m in matricula_crud.listar_matriculas() if m.id_estudiante == est.id_estudiante]
        if matriculas:
            print("  Matrículas:")
            for mat in matriculas:
                print(f"    - {mat}")
        
        # Mostrar promedio del estudiante
        promedio = nota_crud.calcular_promedio(est.id_estudiante)
        print(f"  Promedio: {promedio:.2f}")


def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            menu_estudiantes()
        elif opcion == "2":
            menu_profesores()
        elif opcion == "3":
            menu_facultades()
        elif opcion == "4":
            menu_cursos()
        elif opcion == "5":
            menu_grupos()
        elif opcion == "6":
            menu_evaluaciones()
        elif opcion == "7":
            menu_periodos()
        elif opcion == "8":
            menu_matriculas()
        elif opcion == "9":
            menu_notas()
        elif opcion == "10":
            ver_promedio_estudiante()
        elif opcion == "11":
            listar_estudiantes_relaciones()
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("✗ Opción inválida")


if __name__ == "__main__":
    main()

