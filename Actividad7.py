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
                    for v in range(CantidadCuros):
                        print(f"\n Curso {v + 1}")
                        CodigoCurso = int(input("Ingrese el codigo del curso"))
                        if CodigoCurso in estudiantes:
                            print("El codigo del curso ya esta ingresado no puede repetir un ingreso")
                        else:
                            NombreCurso = input("Ingrese el nombre del curso que deseea inscribir: ")
                            NotaTarea = int(input("Ingrese la nota de Tareas"))
                            if NotaTarea < 0:
                                print("La nota no puede ser negativa")
                            else:
                                NotaParcial = int(input("Ingrese la nota de los parciales"))
                                if NotaParcial < 0:
                                    print("La nota no puede ser negativa")
                                else:
                                    NotaProyecto = int(input("Ingrese la nota de la proyecto"))
                                    if NotaProyecto < 0:
                                        print("La nota no puede ser negativa")
                                    else:
                                        print("Estudiantes Registrados correctamente")
            estudiantes[Carnet] = {
                "Nombre": Nombre,
                "Edad": Edad,
                "Carrera": Carrera,
                "CursosTotales" : {
                    "CodigoCurso": CodigoCurso,
                    "NombreCurso": NombreCurso,
                    "NotaParcial": NotaParcial,
                    "NotaProyecto": NotaProyecto,
                    "NotaTarea": NotaTarea,

                }
            }
        case 2:
            print("Mostrar los estudiantes")
            print("Total estudiantes ")






