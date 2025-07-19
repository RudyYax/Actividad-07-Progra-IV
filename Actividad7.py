estudiantes = {}
opcion = 0
while opcion != 4:
    print("Actividad 07")
    print("-----Bienvenidos-----")
    print("<<<<REGISTRO ESTUDIANTES UNIVERSITARIOS>>>>")
    print("1.- Registrar estudiante")
    print("2.- Mostrar todos los estudiantes y sus curos")
    print("3.- Buscar estudiante por numero de carnet")
    print("4.- Salir")
    opcion = int(input("Ingrese la opcion que desee: "))
    match(opcion):
        case 1:
            print("Bienvenido")
            print("Registrar estudiante")
            cantidad = int(input(f" \n Ingese Cantidad de estudiantes: "))
            for i in range(cantidad):
                print(f" \n Estudiante {i + 1}")
                Carnet = input("Ingrese carnet del estudiante: ")
                if Carnet in estudiantes:
                    print("El carnet ya esta ingresado no puede repetir un ingreso")
                else:
                    Nombre = input("Ingrese el nombre completo del estudiante: ")
                    Edad = input("Ingrese la edad del estudiante: ")
                    Carrera = input("Ingrese la carrera del estudiante: ")
                    CantidadCuros = int(input("Ingrese la cantidad de curos que deseea inscribir: "))

                    estudiantes[Carnet] = {
                        "Nombre": Nombre,
                        "Edad": Edad,
                        "Carrera": Carrera,
                        "Cursos" : {}
                    }
                    for v in range(CantidadCuros):
                        print(f"\n Curso {v + 1}")
                        Codigo_Curso = int(input("Ingrese el codigo del curso"))
                        if Codigo_Curso in estudiantes:
                            print("El codigo del curso ya esta ingresado no puede repetir un ingreso")
                        else:
                            Nombre_Curso = input("Ingrese el nombre del curso que deseea inscribir: ")
                            Nota_Tarea = int(input("Ingrese la nota de Tareas"))
                            if Nota_Tarea < 0:
                                print("La nota no puede ser negativa")
                            else:
                                Nota_Parcial = int(input("Ingrese la nota de los parciales"))
                                if Nota_Parcial < 0:
                                    print("La nota no puede ser negativa")
                                else:
                                    Nota_Proyecto = int(input("Ingrese la nota de la proyecto"))
                                    if Nota_Proyecto < 0:
                                        print("La nota no puede ser negativa")
                                    else:
                                        print("Estudiantes Registrados correctamente")
                    estudiantes[Carnet]["Cursos"][Codigo_Curso] = {
                        "NombreCurso": Nombre_Curso,
                        "NotaTarea": Nota_Tarea,
                        "NotaParcial": Nota_Parcial,
                        "NotaProyecto": Nota_Proyecto
                    }
        case 2:
            print("Mostrar los estudiantes")
            print("Total estudiantes Registrados")
            for carnet, datos in estudiantes.items():
                print(f"Carnet: {carnet}")
                print(f"Nombre : {datos['Nombre']}")
                print(f"Edad: {datos['Edad']}")
                print(f"Carrera: {datos['Carrera']}")
                for Codigo_Curso, curso in datos["Cursos"].items():
                    print(f"Codigo del curso: {Codigo_Curso}")
                    print(f"Nombre del curso: {curso['NombreCurso']}")
                    print(f"Nota del parcial {curso['NotaParcial']}")
                    print(f"Nota del proyecto {curso['NotaProyecto']}")
                    print(f"Nota de las Tareras {curso['NotaTarea']}")
        case 3:
            carnet_buscar = input("Ingrese el carnet del estudiante a buscar: ")
            if carnet_buscar in estudiantes:
                datos = estudiantes[carnet_buscar]
                print(f"\nCarnet: {carnet_buscar}")
                print(f"Nombre: {datos['Nombre']}")
                print(f"Edad: {datos['Edad']}")
                print(f"Carrera: {datos['Carrera']}")
                print("Cursos:")
                if not datos["Cursos"]:
                    print("  No hay cursos inscritos.")
                else:
                    for codigo, curso in datos["Cursos"].items():
                        print(f"  Código del curso: {codigo}")
                        print(f"    Nombre del curso: {curso['NombreCurso']}")
                        print(f"    Nota del parcial: {curso['NotaParcial']}")
                        print(f"    Nota del proyecto: {curso['NotaProyecto']}")
                        print(f"    Nota de las tareas: {curso['NotaTarea']}")
            else:
                print("Carnet no encontrado.")

        case 4:
            print("Saliendo del programa...")

        case _:
            print("Opción inválida, intente de nuevo.")







