estudiantes = {}
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
            Nombre = input("Ingrese el nombre completo del estudiante: ")
            Edad = input("Ingrese la edad del estudiante: ")
            Carrera = input("Ingrese la carrera del estudiante: ")
            CantidadCuros = input("Ingrese la cantidad de curos que deseea inscribir: ")
            for i in range(CantidadCuros):
                print(f"\n Curso {i + 1}")
                NombreCurso = input("Ingrese el nombre del curso que deseea inscribir: ")
                NotaTarea =




