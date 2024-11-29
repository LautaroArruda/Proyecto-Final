from BD.conexion import Conexion
import funciones
import os

def menuPrincipal():
    while True:
        print("\nEscuela Privada")
        print("[1]. Ingresar datos")
        print("[2]. Modificar datos")
        print("[3]. Mostrar datos")
        print("[4]. Eliminar datos")
        print("[5]. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion < 1 or opcion > 5:
            print("Opción incorrecta, ingrese nuevamente.")
        elif opcion == 5:
            print("Saliendo del sistema")
            break
        else:
            ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    if opcion == 1:
        os.system("cls")
        print("¿Qué datos desea ingresar?")
        print("[1]. Ingresar datos de alumnos")
        print("[2]. Ingresar datos de profesores")
        print("[3]. Volver al menú principal")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            os.system("cls")
            funciones.ingresarAlumnos()
        elif opcion == 2:
            os.system("cls")
            funciones.ingresarProfesor()
        else:
            os.system("cls")
    elif opcion == 2:
        os.system("cls")
        print("¿Qué datos desea modificar?")
        print("[1]. Modificar datos de alumnos")
        print("[2]. Modificar datos de profesores")
        print("[3]. Volver al menú principal")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            os.system("cls")
            print("Alumnos")
            print("[1]. Modificar todos los datos")
            print("[2]. Modificar un dato específico")
            print("[3]. Volver al menu")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                funciones.modificarAlumno()
            elif opcion == 2:
                funciones.modificarAlumnoEspecifico()
            elif opcion == 3:
                os.system("cls")
                print("Volviendo al menu")
        elif opcion == 2:
            os.system("cls")
            print("Profesores")
            print("[1]. Modificar todos los datos")
            print("[2]. Modificar un dato específico")
            print("[3]. Volver al menu")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                os.system("cls")
                funciones.modificarProfesor()
            elif opcion == 2:
                os.system("cls")
                funciones.modificarProfesorEspecifico()
            elif opcion == 3:
                os.system("cls")
                print("Volviendo al menu")
        else:
            os.system("cls")
    # Mostrar datos        
    elif opcion == 3:  
        while True:
            os.system("cls")
            print("\nElija una opción")
            print("[1]. Mostrar todos los datos de alumnos")
            print("[2]. Mostrar todos los datos de profesores")
            print("[3]. Buscar en específico")
            print("[4]. Atrás")
            opcion = int(input("Seleccione una opción: "))

            # Mostrar datos del alumno y ordenamiento alfabeticamente   
            if opcion == 1:
                os.system("cls")
                while True:
                    print("Datos de los alumnos\n") 
                    print("[1]. Mostrar todos los datos de los alumnos.")
                    print("[2]. Mostrar alumnos ordenados alfabeticamente.")
                    print("[3]. Atrás")
                    opcion2 = int(input("Seleccione una opcion: "))

                    if opcion2 == 1:
                        os.system("cls")
                        funciones.mostrarDatosAlumnos() 
                    elif opcion2 == 2:
                        os.system("cls")
                        funciones.mostrarAlumnosOrdenados()  
                    elif opcion2 == 3:
                        print("Volviendo")
                        break
                    else:
                        print("Opción inválida")
                            
            # Mostrar datos del profesor y ordenamiento alfabeticamente          
            if opcion == 2:
                os.system("cls")
                while True:
                    print("Datos de los profesores\n") 
                    print("[1]. Mostrar todos los datos de los profesores.")
                    print("[2]. Mostrar profesores ordenados alfabeticamente.")
                    print("[3]. Atrás")
                    opcion2 = int(input("Seleccione una opcion: "))

                    if opcion2 == 1:
                        os.system("cls")
                        funciones.mostrarDatosProfesores() 
                    elif opcion2 == 2:
                        os.system("cls")
                        funciones.mostrarProfesoresOrdenados()  
                    elif opcion2 == 3:
                        print("Volviendo")
                        break
                    else:
                        print("Opción no válida")

            # Buscar un dato en específico con el filtro de búsqueda
            elif opcion == 3:  
                while True:
                    print("\n¿De quién quiere ver sus datos?")
                    print("[1]. Alumno")
                    print("[2]. Profesor")
                    print("[3]. Atrás")
                    opcion = int(input("Seleccione una opción: "))
                    # Buscar datos de alumno
                    if opcion==1:
                        os.system("cls")
                        print("¿Qué datos desea ver?")
                        print("[1]. Buscar por legajo")
                        print("[2]. Buscar por DNI")
                        print("[3]. Buscar por nombre")         
                        print("[4]. buscar por apellido")
                        print("[5]. Buscar por género")
                        print("[6]. Volver al menú principal")
                        opcion2 = int(input("Seleccione una opción: "))

                        # Legajo alumno
                        if(opcion2 ==1):
                            comandoSQL = "legajo"
                            dato= input("Ingresar legajo del alumno: ").strip()
                            while(not dato.isdigit()):
                                print("El legajo debe contener solo digitos.")
                                dato = input("Ingrese el legajo del alumno: ").strip()
                            funciones.buscarEspecificoAlumnos(dato, comandoSQL)

                        # DNI alumno
                        elif opcion2 == 2:
                            comandoSQL = "dni"
                            dato = input("Ingrese el DNI del alumno: ").strip()
                            if len(dato) !=8 or not dato.isdigit():
                                while(len(dato) !=8 or not dato.isdigit()):
                                    print("El DNI debe contener 8 digitos.")
                                    dato = input("Ingrese el DNI del alumno: ").strip()
                            funciones.buscarEspecificoAlumnos(dato, comandoSQL)

                        # Nombre alumno
                        elif opcion2 ==3:
                            comandoSQL="nombre"
                            dato = input("Ingrese el nombre del alumno: ").strip()
                            while not dato.isalpha():
                                print("Por favor, solo ingrese caracteres.")
                                dato = input("Ingresar nombre del alumno: ").strip()
                            funciones.buscarEspecificoAlumnos(dato.title(), comandoSQL)

                        # Apellido alumno
                        elif opcion2 ==4:
                            comandoSQL = "apellido"
                            dato = input("Ingrese el apellido del alumno: ").strip()
                            while not dato.isalpha():
                                print("Por favor, solo ingrese caracteres.")
                                dato = input("Ingrese el apellido del alumno: ").strip()
                            funciones.buscarEspecificoAlumnos(dato.title(), comandoSQL)

                        # Género alumno
                        if(opcion2 ==5):
                            comandoSQL = "genero"
                            opciones_validas = ["Masculino", "Femenino", "Transgenero", "No binario"]
                            dato = input("Ingresar género (Masculino / Femenino / Transgénero / No binario): ").capitalize()

                            while not dato.replace(" ", "").isalpha() or dato not in opciones_validas:
                                print("Por favor, solo ingresar caracteres.")
                                dato = input("Ingresar género (Masculino / Femenino / Transgénero / No binario): ").capitalize()
                            funciones.buscarEspecificoAlumnos(dato, comandoSQL)
                        elif opcion2 == 6:
                            print("Volviendo")
                            break

                    elif opcion == 2:
                        os.system("cls")
                        print("¿Qué datos desea ver?")
                        print("[1]. Buscar por legajo")
                        print("[2]. Buscar por DNI")
                        print("[3]. Buscar por nombre")
                        print("[4]. Buscar por apellido")
                        print("[5]. Buscar por matrícula")
                        print("[6]. Volver al menú principal")
                        opcion2 = int(input("Seleccione una opción: "))

                        # ID profesor
                        if opcion2 == 1 :
                            comandoSQL = "idProfesor"
                            dato = input ("Ingrese ID del profesor: ").strip()
                            while not dato.isdigit():
                                print("Por favor, solo ingresar números.")
                                dato = input ("Ingresar ID del profesor: ").strip()
                            funciones.buscarEspecificoProfesor(dato, comandoSQL)
                                
                        # DNI profesor
                        elif opcion2 == 2 :
                            comandoSQL = "dni"
                            dato = input("Ingrese DNI del profesor: ").strip()
                            if  len(dato) !=8 or not dato.isdigit():
                                while(len(dato) !=8 or not dato.isdigit()):
                                    print("El DNI debe contener 8 digitos.")
                                    dato = input("Ingrese el DNI del profesor: ").strip()
                            funciones.buscarEspecificoProfesor(dato, comandoSQL)

                        # Nombre profesor
                        elif opcion2 == 3 :
                            comandoSQL = "nombre"
                            dato = input("Ingrese el nombre del profesor: ").strip()
                            while not dato.isalpha():
                                print("Por favor, solo ingrese caracteres.")
                                dato = input("Ingrese nombre del profesor: ").strip()
                            funciones.buscarEspecificoProfesor(dato.title(), comandoSQL)

                        # Apellido profesor
                        elif opcion2 == 4 :
                            comandoSQL = "apellido"
                            dato = input("Ingrese el apellido del profesor: ").strip()
                            while not dato.isalpha():
                                print("Por favor, solo ingrese caracteres.")
                                dato = input("Ingrese el apellido del profesor: ").strip()
                            funciones.buscarEspecificoProfesor(dato.title(), comandoSQL)
                        
                        # Matricula profesor
                        elif(opcion2 == 5):
                            comandoSQL = "matricula"
                            dato = input ("Ingresar la matrícula del profesor: ").strip()

                            while not dato.isalnum():
                                print("Por favor, solo ingresar caracteres alfanuméricos.")
                                dato = input("Ingresar la matrícula del profesor: ").strip()
                            funciones.buscarEspecificoProfesor(dato, comandoSQL)
                        #Volver a atras    
                        elif opcion == 6:
                            print("Volviendo")
                            break
                    elif opcion == 3:
                        print("Volviendo")
                        break
            elif opcion == 4:
                os.system("cls")
                print("Volviendo")
                break
            else:
                print("Opción no válida")                        
    # Eliminar datos
    elif opcion == 4:  
        while True:
            print("\n¿A quién desea dar de baja?")
            print("[1]. Dar de baja a un alumno")
            print("[2]. Dar de baja a un profesor")
            print("[3]. Atrás")
            opcion = int(input("Seleccione una opción: "))
            # Eliminar Alumno
            if opcion == 1:
                funciones.listaAlumnos()
                dato = input("Ingrese el legajo del alumno que desea eliminar: ").strip()
                while not dato.isdigit() :
                    print("El legajo tiene que contener sólo 5 números enteros.")
                    dato = input("Ingrese el legajo del alumno que desea eliminar: ").strip()
                funciones.eliminarAlumno(dato)
                
            # Eliminar Profesor                
            elif opcion ==2:    
                funciones.listaProfesores()
                dato = input("Ingrese el ID del profesor que desea eliminar: ").strip()
                while not dato.isdigit():
                    print("El ID tiene que contener solo números enteros.")
                    dato = input("Ingrese el ID del profesor que desea eliminar: ").strip()   
                funciones.eliminarProfe(dato)

            # Volver al menú principal 
            elif opcion == 3:
                os.system("cls")
                print("Volviendo al menú principal")
                break
            else:
                print("Opción no válida")
# Ejecutar el menu principal
menuPrincipal()