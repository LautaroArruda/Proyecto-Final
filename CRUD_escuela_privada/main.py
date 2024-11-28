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
            print("Opcion incorrecta, ingrese nuevamente")
        elif opcion == 5:
            print("Saliendo del sistema")
            break
        else:
            ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    if opcion == 1:
        # Limpiar la consola
        os.system("cls")
        print("Que datos desea ingresar?")
        print("[1]. Ingresar datos de Alumnos")
        print("[2]. Ingresar datos de Profesores")
        print("[3]. Volver al menu principal")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            # Limpiar la consola
            os.system("cls")
            funciones.ingresarAlumnos()
        elif opcion == 2:
            # Limpiar la consola
            os.system("cls")
            funciones.ingresarProfesor()
        else:
            # Limpiar la consola
            os.system("cls")
    elif opcion == 2:
        # Limpiar la consola
        os.system("cls")
        print("Que datos desea modificar?")
        print("[1]. modificar datos de Alumnos")
        print("[2]. modificar datos de Profesores")
        print("[3]. Volver al menu principal")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            # Limpiar la consola
            os.system("cls")
            print("Alumnos")
            print("[1]. modificar todos los datos")
            print("[2]. modificar un dato específico")
            print("[3]. volver atras")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                funciones.modificarAlumno()
            elif opcion == 2:
                funciones.modificarAlumnoEspecifico()
        elif opcion == 2:
            # Limpiar la consola
            os.system("cls")
            print("Profesores")
            print("[1]. modificar todos los datos")
            print("[2]. modificar un dato específico")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                # Limpiar la consola
                os.system("cls")
                funciones.modificarProfesor()
            elif opcion == 2:
                # Limpiar la consola
                os.system("cls")
                funciones.modificarProfesorEspecifico() 
        else:
            # Limpiar la consola
            os.system("cls")        
    elif opcion == 3:  # Mostrar datos
        while True:
            # Limpiar la consola
            os.system("cls")
            print("\nElija una opción")
            print("[1]. Mostrar todos los datos de alumnos")
            print("[2]. Mostrar todos los datos de profesores")
            print("[3]. Buscar en específico")
            print("[4]. Atrás")
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                print("Ver alumnos")  # Llama a la funcion mostrar todos los alumnos
            elif opcion == 2:
                print("Ver profesores")  # Llama a la funcion mostrar todos los profesores
            elif opcion == 3:  # Buscar en especifico
                while True:
                    print("\n¿De quien quiere ver sus datos?")
                    print("[1]. Alumno")
                    print("[2]. Profesor")
                    print("[3]. Atrás")
                    opcion = int(input("Seleccione una opcion: "))
                    # Buscar datos de alumno
                    if opcion==1:
                        # Limpiar la consola
                        os.system("cls")
                        print("Que datos desea ver?")
                        print("[1]. Buscar por legajo")
                        print("[2]. Buscar por DNI")
                        print("[3]. Buscar por Nombre")         
                        print("[4]. buscar por apellido")
                        print("[5]. Buscar por genero")
                        print("[6]. Volver al menu principal")
                        opcion2 = int(input("Seleccione una opción: "))
                        #Legajo alumno
                        if(opcion2 ==1):
                            comandoSQL = "legajo"
                            dato= input("Ingresar legajo: ").strip()
                            #Legajo alumno
                            while(not dato.isdigit()):
                                print("El legajo debe contener solo digitos.")
                                dato = input("Ingrese el legajo: ").strip()
                            funciones.buscarEspecificoAlumnos(dato, comandoSQL)

                        #DNI alumno
                        elif opcion2 == 2:
                            comandoSQL = "dni"
                            dato = input("Ingrese el DNI: ").strip()
                            if len(dato) !=8 or not dato.isdigit():
                                while(len(dato) !=8 or not dato.isdigit()):
                                    print("El DNI debe contener 8 digitos.")
                                    dato = input("Ingrese el DNI: ").strip()
                            funciones.buscarEspecificoAlumnos(dato, comandoSQL)

                        #Nombre alumno
                        elif opcion2 ==3:
                            comandoSQL="nombre"
                            dato = input("Ingrese el nombre: ").strip()
                            while not dato.isalpha():
                                print("Por favor, solo ingrese caracteres.")
                                dato = input("Ingresar nombre: ").strip()
                            funciones.buscarEspecificoAlumnos(dato.title(), comandoSQL)

                        #Apellido alumno
                        elif opcion2 ==4:
                            comandoSQL = "apellido"
                            dato = input("Ingresar apellido: ").strip()
                            while not dato.isalpha():
                                print("Por favor, solo ingrese caracteres.")
                                dato = input("Ingresar apellido: ").strip()
                            funciones.buscarEspecificoAlumnos(dato.title(), comandoSQL)

                        #Genero alumno
                        if(opcion2 ==5):
                            comandoSQL = "genero"
                            opciones_validas = ["Masculino", "Femenino", "Transgenero", "No binario"]
                            dato = input("Ingresar genero (masculino, femenino, transgero y no binario): ").capitalize()

                            while not dato.replace(" ", "").isalpha() or dato not in opciones_validas:
                                print("Porfavor solo ingresar caracteres.")
                                dato = input("Ingresar genero (masculino, femenino, transgero y no binario): ").capitalize()
                            funciones.buscarEspecificoAlumnos(dato, comandoSQL)
                        elif opcion2 == 6:
                            print("Volviendo")
                            break
                        else:
                            print("Opcion invalida")
                    elif opcion == 2:
                        # Limpiar la consola
                        os.system("cls")
                        print("Que datos desea ver?")
                        print("[1]. Buscar por legajo")
                        print("[2]. Buscar por DNI")
                        print("[3]. Buscar por Nombre")
                        print("[4]. buscar por apellido")
                        print("[5]. Buscar por matricula")
                        print("[6]. Volver al menu principal")
                        opcion2 = int(input("Seleccione una opción: "))

                        #Legajo profesor
                        if opcion2 == 1 :
                            comandoSQL = "idProfesor"
                            dato = input ("Ingresar ID de profesor: ").strip()
                            while not dato.isdigit():
                                print("porfavor solo ingresar numeros")
                                dato = input ("Ingresar legajo: ").strip()
                            funciones.buscarEspecificoProfesor(dato, comandoSQL)
                                
                        #DNI profesor
                        elif opcion2 == 2 :
                            comandoSQL = "dni"
                            dato = input("Ingresar DNI: ").strip()
                            if  len(dato) !=8 or not dato.isdigit():
                                while(len(dato) !=8 or not dato.isdigit()):
                                    print("El legajo debe contener 8 digitos.")
                                    dato = input("Ingrese el legajo: ").strip()
                            funciones.buscarEspecificoProfesor(dato, comandoSQL)

                        #Nombre profesor
                        elif opcion2 == 3 :
                            comandoSQL = "nombre"
                            dato = input("Ingresar nombre: ").strip()
                            while not dato.isalpha():
                                print("Por favor, solo ingrese caracteres.")
                                dato = input("Ingresar nombre: ").strip()
                            funciones.buscarEspecificoProfesor(dato.title(), comandoSQL)

                        #Apellido profesor
                        elif opcion2 == 4 :
                            comandoSQL = "apellido"
                            dato = input("Ingresar apellido").strip()
                            while not dato.isalpha():
                                print("Por favor, solo ingrese caracteres.")
                                dato = input("Ingresar apellido: ").strip()
                            funciones.buscarEspecificoProfesor(dato.title(), comandoSQL)
                        
                        #Matricula profesor
                        elif(opcion2 == 5):
                            comandoSQL = "matricula"
                            dato = input ("Ingresar matricula: ").strip()

                            while not matricula.isalnum():
                                print("Porfavor solo ingresar caracteres alfanumerico.")
                                matricula = input("Ingresar matricula: ").strip()
                            funciones.buscarEspecificoProfesor(dato, comandoSQL)
                        #Volver a atras    
                        elif opcion == 6:
                            print("Volviendo")
                            break
                    elif opcion == 3:
                        print("Volviendo")
                        break
                    else:
                        print("Opcion invalida")
            elif opcion == 4:
                # Limpiar la consola
                os.system("cls")
                print("Volviendo")
                break
            else:
                print("Opcion invalida")                        
    # Eliminar datos
    elif opcion == 4:  
        while True:
            # Limpiar la consola
            print("\n¿A quién desea dar de baja?")
            print("[1]. Dar de baja a un alumno")
            print("[2]. Dar de baja a un profesor")
            print("[3]. Atras")
            opcion = int(input("Seleccione una opción: "))
            #Eliminar Alumno
            if opcion == 1:
                # Limpiar la consola
                funciones.motrarAlumnos()
                dato = input("Ingrese el legajo del Alumno que desea eliminar: ").strip()
                while not dato.isdigit() :
                    print("El Legajo tiene que contener solo 5 numeros enteros")
                    dato = input("Ingrese el Legajo del Alumno que desea eliminar: ").strip()
                funciones.eliminarAlumno(dato)
                
            #Eliminar Profesor                
            elif opcion ==2:
                # Limpiar la consola    
                funciones.motrarProfes()
                dato = input("Ingrese el ID del Profesor que desea eliminar: ").strip()
                while not dato.isdigit():
                    print("El id tiene que contener solo numeros enteros")
                    dato = input("Ingrese el ID del Profesor que desea eliminar: ").strip()   
                funciones.eliminarProfe(dato)

            #Volver al menu principal 
            elif opcion == 3:
                # Limpiar la consola
                os.system("cls")
                print("Volviendo al menú principal")
                break
            else:
                print("Opcion no valida")
# Ejecutar el menu principal
menuPrincipal()
