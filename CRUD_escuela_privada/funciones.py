import mysql.connector
from BD.conexion import Conexion
import os
import re

# -----------> Colores <-----------

class c:
    verde = '\033[96m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    quit = '\033[0m'
    bold = '\033[1m'

# ----------------- INGRESO DE DATOS -----------------

# -----> Ingreso de datos del alumno <------

def ingresarAlumnos():
    try:
        # Crear una instancia de la conexión
        conexion_instancia = Conexion()
        conexion = conexion_instancia.conexionBD()
        cursor = conexion.cursor()

        # Ingreso de nombre del alumno
        nombre = input("Ingrese el nombre del alumno: ").strip() # strip elimina los espacios vacios que están antes y después del string
        while not nombre.isalpha() or len(nombre) < 2:  # isalpha acepta sólo letras de la a-z
            print(c.rojo + "Por favor, sólo ingrese caracteres." + c.quit)
            nombre = input("Ingrese el nombre del alumno: ").strip()

        # Ingreso de apellido del alumno
        apellido = input("Ingrese el apellido del alumno: ").strip()
        while not apellido.isalpha() or len(apellido) < 2:  # len nos da la longitud del dato ingresado
            print(c.rojo + "Por favor, sólo ingrese caracteres." + c.quit)
            apellido = input("Ingrese el apellido del alumno: ").strip()

        # Ingreso de DNI del alumno
        dni = input("Ingrese el DNI del alumno: ").strip()
        if len(dni) != 8 or not dni.isdigit():  # isdigit acepta sólo números
            while (len(dni) != 8 or not dni.isdigit()):
                print(c.rojo +"El DNI debe contener 8 digitos."+ c.quit)
                dni = input("Ingrese el DNI del alumno: ").strip()

        # Ingreso de direccion del alumno
        direccion = input("Ingrese la dirección del alumno: ").strip()
        while len(direccion) < 3 or direccion.isdigit():
            if direccion.isdigit():
                print(c.rojo +"Por favor, ingrese una dirección válida."+ c.quit)
                direccion = input("Ingrese la dirección del alumno: ").strip()

        # Ingreso de género del alumno
        opciones_validas = ["Masculino","Femenino", "Transgenero", "No binario"] # capitalize pone la primera letra en mayúscula
        genero = input("Ingresar género (Masculino / Femenino / Transgénero / No binario): ").capitalize()
        while not genero.replace(" ", "").isalpha() or genero not in opciones_validas: # replace reemplaza un caracter por otro
            print(c.rojo +"Por favor, sólo ingresar masculino / femenino / transgénero / no binario." + c.quit)
            genero = input("Ingresar género (Masculino / Femenino / Transgénero / No binario): ").capitalize()

        # Ingreso de la fecha de nacimiento del alumno
        # Ingreso de año
        print("Ingrese la fecha de nacimiento (YYYY-MM-DD) del alumno:\n")
        año = input("Ingrese el año (entre 2004 y 2010): ").strip()
        while not año.isdigit() or not (2004 <= int(año) <= 2010):
            print(c.rojo +"Por favor, ingrese un número válido entre 2004 y 2010."+ c.quit)
            año = input("Ingrese el año (entre 2004 y 2010): ").strip()
        # Ingreso de mes
        mes = input("Ingrese el mes: ").strip()
        while not mes.isdigit() or not (1 <= int(mes) <= 12):
            print(c.rojo +"Por favor, ingrese un número válido entre 1 y 12."+ c.quit)
            mes = input("Ingrese el mes: ").strip()
        # Ingreso de día
        dia = input("Ingrese el día: ").strip()
        while not dia.isdigit() or not (1 <= int(dia) <= 31):
            print(c.rojo +"Por favor, ingrese un número válido entre 1 y 31."+ c.quit)
            dia = input("Ingrese el día: ")

        fechaNacimiento = año + "-" + mes + "-" + dia

        # Ingreso del email del alumno
        emailValido = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$' 
        while True:
            email = input("Ingrese el email del alumno: ").strip().lower() # lower convierte todas las letras del string en minúscula
            if re.match(emailValido, email): # verifica que el correo ingresado sea válido utilizando la librería re
                break  # si el correo ingresado es válido pasa
            else:
                print(c.rojo +"Ingrese un correo electrónico que sea válido."+ c.quit)

        # Ingreso del curso del alumno
        cursos_idCurso = input("Ingrese el número del curso que pertenece (1-6): ")
        while not cursos_idCurso.isdigit() or int(cursos_idCurso) < 1 or int(cursos_idCurso) > 6:
            print(c.rojo +"El número de curso debe ser entre 1 y 6."+ c.quit)
            cursos_idCurso = input("Ingrese el número del curso al que pertenece (1-6): ")

        # Consulta SQL para insertar datos
        sql = """INSERT INTO alumnos (nombre, apellido, dni, direccion, genero,
                 fechaNacimiento, email, cursos_idCurso)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (nombre.title(), apellido.title(), dni, direccion.title(),
                   genero, fechaNacimiento, email.lower(), cursos_idCurso)

        # Ejecutar la consulta
        cursor.execute(sql, valores)
        conexion.commit()  # commit confirma los cambios en la base de datos
        os.system("cls") # limpiar la consola
        print(c.verde +f"{cursor.rowcount} registro(s) ingresado(s) exitosamente."+ c.quit) # rowcount devuelve el numero de las filas afectadas

    except Exception as e:
        print(c.rojo +f"Error al ingresar datos: {e}"+ c.quit)
    finally:
        cursor.close()
        conexion.close()

# -----> Ingreso de datos del profesores <------


def ingresarProfesor():
    try:
        conexion_instancia = Conexion()
        conexion = conexion_instancia.conexionBD()
        cursor = conexion.cursor()

        # Ingreso nombre del profesor
        nombre = input("Ingrese el nombre del profesor: ").strip()
        while not nombre.isalpha() or len(nombre) < 2:
            print(c.rojo +"Por favor, sólo ingrese caracteres."+ c.quit)
            nombre = input("Ingrese el nombre del profesor: ").strip()

        # Ingreso apellido del profesor
        apellido = input("Ingrese el apellido del profesor: ").strip()
        while not apellido.isalpha() or len(apellido) < 2:
            print(c.rojo +"Por favor, sólo ingrese caracteres."+ c.quit)
            apellido = input("Ingrese el apellido del profesor: ").strip()

        # Ingreso teléfono del profesor
        telefono = input("Ingrese el teléfono del profesor: ").strip()
        if len(telefono) != 10 or not telefono.isdigit():
            while (len(telefono) != 10 or not telefono.isdigit()):
                print(c.rojo +"El teléfono debe contener 10 dígitos."+ c.quit)
                telefono = input("Ingrese el telefono del profesor: ").strip()

        emailValido = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$' 
        while True:
            email = input("Ingrese el email del profesor: ").strip().lower() # lower convierte todas las letras del string en minúscula
            if re.match(emailValido, email): # verifica que el correo ingresado sea válido utilizando la librería re
                break  # si el correo ingresado es válido pasa
            else:
                print(c.rojo +"Ingrese un correo electrónico que sea válido."+ c.quit)

        # Ingreso DNI del profesor
        dni = input("Ingrese el DNI del profesor: ").strip()
        if len(dni) != 8 or not dni.isdigit():
            while (len(dni) != 8 or not dni.isdigit()):
                print(c.rojo +"El DNI debe contener 8 digitos."+ c.quit)
                dni = input("Ingrese el DNI del profesor: ").strip()

        # Ingreso de la fecha de nacimiento del profesor
        # Ingreso de año
        print("Ingrese la fecha de nacimiento (YYYY-MM-DD) del profesor:\n")
        año = input("Ingrese el año (entre 1950 y 2004): ").strip()
        while not año.isdigit() or not (1950 <= int(año) <= 2004):
            print(c.rojo +"Por favor, ingrese un número válido entre 1950 y 2004."+ c.quit)
            año = input("Ingrese el año (entre 1950 y 2004): ").strip()
        # Ingreso de mes
        mes = input("Ingrese el mes: ").strip()
        while not mes.isdigit() or not (1 <= int(mes) <= 12):
            print(c.rojo +"Por favor, ingrese un número válido entre 1 y 12."+ c.quit)
            mes = input("Ingrese el mes: ").strip()
        # Ingreso de día
        dia = input("Ingrese el día: ").strip()
        while not dia.isdigit() or not (1 <= int(dia) <= 31):
            print(c.rojo +"Por favor, ingrese un número válido entre 1 y 31."+ c.quit)
            dia = input("Ingrese el día: ")

        fechaNacimiento = año + "-" + mes+ "-" + dia

        # Ingreso de la matrícula del profesor
        matricula = input("Ingrese la matrícula del profesor: ").strip()
        while not matricula.isalnum():
            print(c.rojo +"Por favor, sólo ingresar caracteres alfanumérico."+ c.quit)
            matricula = input("Ingresar la matrícula del profesor: ").strip()

        # Ingreso de la dirección del profesor
        direccion = input("Ingrese la dirección del profesor: ").strip()
        while len(direccion) < 3 or direccion.isdigit():
            if direccion.isdigit():
                print(c.rojo +"Por favor, ingrese una dirección válida."+ c.quit)
                direccion = input("Ingrese la dirección del profesor: ").strip()

        # Ingreso de las horas del profesor
        horas = input("Ingrese las horas del profesor: ").strip()
        if len(dni) < 1 or not dni.isdigit():
            while (len(dni) < 1 or not dni.isdigit()):
                print(c.rojo +"Las horas no pueden ser menores a 1."+ c.quit)
                dni = input("Ingrese las horas del profesor: ").strip()

        # Ingreso del sueldo del profesor
        sueldo = input("Ingrese el sueldo del profesor: $").strip()
        while not sueldo.isdigit() or int(sueldo) <= 200000:
            print(c.rojo +"El sueldo debe ser mayor a $200000."+ c.quit)
            sueldo = input("Ingrese el sueldo del profesor: $").strip()

        # Consulta SQL para insertar datos
        sql = """INSERT INTO profesores (nombre, apellido, telefono, email,
                   dni, fechaNacimiento, matricula, direccion, horas, sueldo)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"""
        valores = (nombre.title(), apellido.title(), telefono, email,
                   dni, fechaNacimiento, matricula, direccion.title(), horas, sueldo)

        # Ejecutar la consulta
        cursor.execute(sql, valores)
        conexion.commit()  # Confirma los cambios en la base de datos
        os.system("cls")  # system("cls") sirve para limpiar la consola
        print(c.verde +f"{cursor.rowcount} registro(s) ingresado(s) exitosamente."+ c.quit) # rowcount devuelve el número de las filas añadidas

    except Exception as e:
        print(c.rojo +f"Error al ingresar datos: {e}"+ c.quit)
    finally:
        cursor.close()
        conexion.close()

# ----------------- MODIFICACIÓN DE DATOS -----------------

# -----> Modificación de todos los datos del alumno <------


def modificarAlumno():
    listaAlumnos()
    try:
        conexion_instancia = Conexion()
        conexion = conexion_instancia.conexionBD()
        cursor = conexion.cursor()

        # Solicitar el legajo del alumno que se desea modificar
        legajo = input("Ingrese el legajo del alumno que desea modificar: ").strip()

        # Verificar si el alumno existe
        select = "SELECT * FROM alumnos WHERE legajo = %s"
        cursor.execute(select, (legajo,))
        resultado = cursor.fetchone() # En Python, el método fetchone() se utiliza para devolver una sola fila de resultados de una consulta SQL
                                      # Obtiene sólo el primer registro de la consulta como tuplas (no son modificables)

        if not resultado:
            print(c.amarillo +"No se encontró un alumno con el legajo proporcionado."+ c.quit)
            return

        os.system("cls")

        # Muestra los datos del alumno a modificar
        print("Datos actuales del alumno: ")
        print(f"\n[1] . Nombre: {resultado[1]}\n[2] . Apellido: {resultado[2]}\n[3] . DNI: {resultado[3]}")
        print(f"[4] . Dirección: {resultado[4]}\n[5] . Género: {resultado[5]}\n[6] . Fecha de Nacimiento: {resultado[6]}")
        print(f"[7] . Email: {resultado[7]}\n[8] . Curso: {resultado[8]}\n")

        # Solicita los nuevos datos para la modificación
        print("\nIngrese los nuevos datos del alumno: ")

        nombre = input("Ingrese el nombre del alumno: ").strip()
        while not nombre.isalpha() or len(nombre) < 2:
            print(c.rojo +"Por favor, sólo ingrese caracteres."+ c.quit)
            nombre = input("Ingrese el nombre del alumno: ").strip()

        apellido = input("Ingrese el apellido del alumno: ").strip()
        while not apellido.isalpha() or len(apellido) < 2:
            print(c.rojo +"Por favor, sólo ingrese caracteres."+ c.quit)
            apellido = input("Ingrese el apellido del alumno: ").strip()

        dni = input("Ingrese el DNI del alumno: ").strip()
        if len(dni) != 8 or not dni.isdigit():
            while (len(dni) != 8 or not dni.isdigit()):
                print(c.rojo +"El DNI debe contener 8 digitos."+ c.quit)
                dni = input("Ingrese el DNI del alumno: ").strip()

        direccion = input("Ingrese la dirección del alumno: ").strip()
        while len(direccion) < 3 or direccion.isdigit():
            if direccion.isdigit():
                print(c.rojo +"Por favor, ingrese una dirección válida."+ c.quit)
                direccion = input("Ingrese la dirección del alumno: ").strip()

        opciones_validas = ["Masculino","Femenino", "Transgenero", "No binario"]
        genero = input("Ingresar el género (Masculino / Femenino / Transgénero / No binario): ").strip()
        while not genero.replace(" ", "").isalpha() or genero not in opciones_validas:
            print(c.rojo +"Por favor, sólo ingresar masculino / femenino / transgénero / no binario."+ c.quit)
            genero = input("Ingresar el género (Masculino / Femenino / Transgénero / No binario): ").capitalize()

        # Ingreso de la fecha de nacimiento del alumno
        # Ingreso de año
        print("Ingrese la fecha de nacimiento (YYYY-MM-DD) del alumno:\n")
        año = input("Ingrese el año (entre 2004 y 2010): ").strip()
        while not año.isdigit() or not (2004 <= int(año) <= 2010):
            print(c.rojo +"Por favor, ingrese un número válido entre 2004 y 2010."+ c.quit)
            año = input("Ingrese el año (entre 2004 y 2010): ").strip()
        # Ingreso de mes
        mes = input("Ingrese el mes: ").strip()
        while not mes.isdigit() or not (1 <= int(mes) <= 12):
            print(c.rojo +"Por favor, ingrese un número válido entre 1 y 12."+ c.quit)
            mes = input("Ingrese el mes: ").strip()
        # Ingreso de día
        dia = input("Ingrese el día: ").strip()
        while not dia.isdigit() or not (1 <= int(dia) <= 31):
            print(c.rojo +"Por favor, ingrese un número válido entre 1 y 31."+ c.quit)
            dia = input("Ingrese el día: ")

        fechaNacimiento = año + "-" + mes+ "-" + dia

        emailValido = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$' 
        while True:
            email = input("Ingrese el email del alumno: ").strip().lower() # lower convierte todas las letras del string en minúscula
            if re.match(emailValido, email): # verifica que el correo ingresado sea válido utilizando la librería re
                break  # si el correo ingresado es válido pasa
            else:
                print(c.rojo +"Ingrese un correo electrónico que sea válido."+ c.quit)

        cursos_idCurso = input("Ingrese el número del curso que pertenece (1-6): ").strip()
        while not cursos_idCurso.isdigit() or int(cursos_idCurso) < 1 or int(cursos_idCurso) > 6:
            print(c.rojo +"El número de curso debe ser entre 1 y 6."+ c.quit)
            cursos_idCurso = input("Ingrese el número del curso que pertenece (1-6): ").strip()

        # Actualizar datos en la base de datos
        sql = """UPDATE alumnos
                        SET nombre = %s, apellido = %s, dni = %s, direccion = %s, genero = %s,
                            fechaNacimiento = %s, email = %s, cursos_idCurso = %s
                        WHERE legajo = %s"""
        valores = (nombre.title(), apellido.title(), dni, direccion.title(), genero,
                   fechaNacimiento, email.lower(), cursos_idCurso, legajo)

        cursor.execute(sql, valores)
        conexion.commit()

        print(c.verde +"Datos del alumno  actualizados correctamente."+ c.quit)

    except Exception as e:
        print(c.rojo +f"Error al modificar los datos: {e}"+ c.quit)
    finally:
        cursor.close()
        conexion.close()

# -----> Modificación de todos los datos del profesor <------


def modificarProfesor():
    listaProfesores()
    try:
        conexion_instancia = Conexion()
        conexion = conexion_instancia.conexionBD()
        cursor = conexion.cursor()

        # Solicitar el id del profesor que se desea modificar
        idProfesor = input("Ingrese el ID del profesor que desea modificar: ").strip()

        # Verificar si el profesor existe
        select = "SELECT * FROM profesores WHERE idProfesor = %s"
        cursor.execute(select, (idProfesor,)) 
        resultado = cursor.fetchone() # En Python, el método fetchone() se utiliza para devolver una sola fila de resultados de una consulta SQL
                                      # Obtiene solo el primer registro de la consulta como tuplas

        if not resultado:
            print(c.amarillo +"No se encontró un profesor con el ID proporcionado."+ c.quit)
            return
        os.system("cls")
        print("Datos actuales del profesor: ")
        print(f"\nID: {resultado[0]}\nNombre: {resultado[1]}\nApellido: {resultado[2]}\nTeléfono: {resultado[3]}")
        print(f"Email: {resultado[4]}\nDNI: {resultado[5]}\nFecha de Nacimiento: {resultado[6]}")
        print(f"Matrícula: {resultado[7]}\nDirección: {resultado[8]}\nHoras: {resultado[9]}\nSueldo: {resultado[10]}")

        # Solicita los nuevos datos para la modificación
        print("\nIngrese los nuevos datos del profesor: ")

        nombre = input("Ingrese el nombre del profesor: ").strip()
        while not nombre.isalpha() or len(nombre) < 2:
            print(c.rojo +"Por favor, sólo ingrese caracteres."+ c.quit)
            nombre = input("Ingrese el nombre del profesor: ").strip()

        apellido = input("Ingrese el apellido del profesor: ").strip()
        while not apellido.isalpha() or len(apellido) < 2:
            print(c.rojo +"Por favor, sólo ingrese caracteres."+ c.quit)
            apellido = input("Ingrese el apellido del profesor: ").strip()

        telefono = input("Ingrese el teléfono del profesor: ").strip()
        if len(telefono) != 10 or not telefono.isdigit():
            while (len(telefono) != 10 or not telefono.isdigit()):
                print(c.rojo +"El teléfono sólo debe contener 10 digitos."+ c.quit)
                telefono = input("Ingrese el telefono del profesor: ").strip()

        emailValido = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$' 
        while True:
            email = input("Ingrese el email del profesor: ").strip().lower() # lower convierte todas las letras del string en minúscula
            if re.match(emailValido, email): # verifica que el correo ingresado sea válido utilizando la librería re
                break  # si el correo ingresado es válido pasa
            else:
                print(c.rojo +"Ingrese un correo electrónico que sea válido."+ c.quit)

        dni = input("Ingrese el DNI del profesor: ").strip()
        if len(dni) != 8 or not dni.isdigit():
            while (len(dni) != 8 or not dni.isdigit()):
                print(c.rojo +"El DNI debe contener 8 digitos."+ c.quit)
                dni = input("Ingrese el DNI del profesor: ").strip()

        # Ingreso de la fecha de nacimiento del profesor
        # Ingreso de año
        print("Ingrese la fecha de nacimiento (YYYY-MM-DD) del profesor:\n")
        año = input("Ingrese el año (entre 1950 y 2004): ").strip()
        while not año.isdigit() or not (1950 <= int(año) <= 2004):
            print(c.rojo +"Por favor, ingrese un número válido entre 1950 y 2004."+ c.quit)
            año = input("Ingrese el año (entre 1950 y 2004): ").strip()
        # Ingreso de mes
        mes = input("Ingrese el mes: ").strip()
        while not mes.isdigit() or not (1 <= int(mes) <= 12):
            print(c.rojo +"Por favor, ingrese un número válido entre 1 y 12."+ c.quit)
            mes = input("Ingrese el mes: ").strip()
        # Ingreso de día
        dia = input("Ingrese el día: ").strip()
        while not dia.isdigit() or not (1 <= int(dia) <= 31):
            print(c.rojo +"Por favor, ingrese un número válido entre 1 y 31."+ c.quit)
            dia = input("Ingrese el día: ")

        fechaNacimiento = año + "-" + mes+ "-" + dia

        matricula = input("Ingrese el matricula del profesor: ")
        while not matricula.isalnum():
            print(c.rojo +"Por favor, sólo ingresar caracteres alfanumérico."+ c.quit)
            matricula = input("Ingrese la matrícula del profesor: ").strip()

        direccion = input("Ingrese la dirección del profesor: ").strip()
        while len(direccion) < 3 or direccion.isdigit():
            if direccion.isdigit():
                print(c.rojo +"Por favor, ingrese una dirección válida."+ c.quit)
                direccion = input("Ingrese la dirección del profesor: ").strip()

        horas = input("Ingrese las horas del profesor: ").strip()
        if len(dni) < 1 or not dni.isdigit():
            while (len(dni) < 1 or not dni.isdigit()):
                print(c.rojo +"Las horas no pueden ser menores a 1."+ c.quit)
                dni = input("Ingrese las horas del profesor: ").strip()

        sueldo = input("Ingrese el sueldo del profesor: $").strip()
        while not sueldo.isdigit() or int(sueldo) <= 200000:
            print(c.rojo +"El sueldo debe ser mayor a $200000."+ c.quit)
            sueldo = input("Ingrese el sueldo del profesor: $").strip()

        # Actualizar datos en la base de datos
        sql = """UPDATE profesores SET nombre = %s, apellido = %s, telefono = %s, email = %s, dni = %s, fechaNacimiento = %s, matricula = %s, direccion = %s , horas = %s ,sueldo = %s  WHERE idProfesor = %s """
        valores = (nombre.title(), apellido.title(), telefono, email.lower(), dni,
                   fechaNacimiento, matricula, direccion.title(), horas, sueldo, idProfesor)

        cursor.execute(sql, valores)
        conexion.commit()

        print(c.verde +"Datos del profesor actualizados correctamente."+ c.quit)

    except Exception as e:
        print(c.rojo +f"Error al modificar los datos: {e}"+ c.quit)
    finally:
        cursor.close()
        conexion.close()

# -----> Modificación un dato en específico del alumno <------


def modificarAlumnoEspecifico():
    listaAlumnos()
    try:
        conexion_instancia = Conexion()
        conexion = conexion_instancia.conexionBD()
        cursor = conexion.cursor()

        # Solicitar el legajo del alumno que se desea modificar
        legajo = input("Ingrese el legajo del alumno que desea modificar: ")

        select = "SELECT * FROM alumnos WHERE legajo = %s"
        cursor.execute(select, (legajo,))
        resultado = cursor.fetchone() # Obtiene solo el primer registro de la consulta como tuplas

        if not resultado:
            print(c.amarillo +"No se encontró un alumno con el legajo proporcionado."+ c.quit)
            return
        os.system("cls")
        print("Datos actuales del alumno: ")
        print(f"\n[1] . Nombre: {resultado[1]}\n[2] . Apellido: {resultado[2]}\n[3] . DNI: {resultado[3]}")
        print(f"[4] . Dirección: {resultado[4]}\n[5] . Género: {resultado[5]}\n[6] . Fecha de Nacimiento: {resultado[6]}")
        print(f"[7] . Email: {resultado[7]}\n[8] . Curso: {resultado[8]}\n")
        menu = int(input("¿Qué dato desea modificar?: ").strip()) # Solicita que dato quiero modificar
        if menu == 1:

            nombre = input("Ingrese el nombre del alumno: ").strip()
            while not nombre.isalpha() or len(nombre) < 2:
                print(c.rojo +"Por favor, solo ingrese caracteres."+ c.quit)
                nombre = input("Ingrese el nombre del alumno: ").strip()

            sql = "UPDATE alumnos SET Nombre = %s WHERE legajo = %s"
            valor = (nombre.title(), legajo)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 2:

            apellido = input("Ingrese el apellido del alumno: ").strip()
            while not apellido.isalpha() or len(apellido) < 2:
                print(c.rojo +"Por favor, solo ingrese caracteres."+ c.quit)
                apellido = input("Ingrese el apellido del alumno: ").strip()

            sql = "UPDATE alumnos SET apellido = %s WHERE legajo = %s"
            valor = (apellido.title(), legajo)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 3:

            dni = input("Ingrese el DNI del alumno: ").strip()
            if len(dni) != 8 or not dni.isdigit():
                while (len(dni) != 8 or not dni.isdigit()):
                    print(c.rojo +"El DNI debe contener 8 digitos."+ c.quit)
                    dni = input("Ingrese el DNI del alumno: ").strip()

            sql = "UPDATE alumnos SET dni = %s WHERE legajo = %s"
            valor = (dni, legajo)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 4:

            direccion = input("Ingrese la dirección del alumno: ").strip()
            while len(direccion) < 3 or direccion.isdigit():
                if direccion.isdigit():
                    print(c.rojo +"Por favor, ingrese una dirección válida."+ c.quit)
                    direccion = input("Ingrese la dirección del alumno: ").strip()

            sql = "UPDATE alumnos SET direccion = %s WHERE legajo = %s"
            valor = (direccion.title(), legajo)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 5:

            opciones_validas = ["Masculino","Femenino", "Transgenero", "No binario"]
            genero = input("Ingresar género (Masculino / Femenino / Transgénero / No binario): ")
            while not genero.replace(" ", "").isalpha() or genero not in opciones_validas:
                print(c.rojo +"Por favor, sólo ingresar masculino / femenino / transgénero / no binario."+ c.quit)
                genero = input("Ingresar género (Masculino / Femenino / Transgénero / No binario): ").capitalize()
            sql = "UPDATE alumnos SET genero = %s WHERE legajo = %s"
            valor = (genero, legajo)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 6:

            # Ingreso de la fecha de nacimiento del alumno
            # Ingreso de año
            print("Ingrese la fecha de nacimiento (YYYY-MM-DD) del alumno:\n")
            año = input("Ingrese el año (entre 2004 y 2010): ").strip()
            while not año.isdigit() or not (2004 <= int(año) <= 2010):
                print(c.rojo +"Por favor, ingrese un número válido entre 2004 y 2010."+ c.quit)
                año = input("Ingrese el año (entre 2004 y 2010): ").strip()
            # Ingreso de mes
            mes = input("Ingrese el mes: ").strip()
            while not mes.isdigit() or not (1 <= int(mes) <= 12):
                print(c.rojo +"Por favor, ingrese un número válido entre 1 y 12."+ c.quit)
                mes = input("Ingrese el mes: ").strip()
            # Ingreso de día
            dia = input("Ingrese el día: ").strip()
            while not dia.isdigit() or not (1 <= int(dia) <= 31):
                print(c.rojo +"Por favor, ingrese un número válido entre 1 y 31."+ c.quit)
                dia = input("Ingrese el día: ")

            fechaNacimiento = año + "-" + mes+ "-" + dia

            sql = "UPDATE alumnos SET fechaNacimiento = %s WHERE legajo = %s"
            valor = (fechaNacimiento, legajo)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 7:

            emailValido = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$' 
            while True:
                email = input("Ingrese el email del alumno: ").strip().lower() # lower convierte todas las letras del string en minúscula
                if re.match(emailValido, email): # verifica que el correo ingresado sea válido utilizando la librería re
                    break  # si el correo ingresado es válido pasa
                else:
                    print(c.rojo +"Ingrese un correo electrónico que sea válido."+ c.quit)

            sql = "UPDATE alumnos SET email = %s WHERE legajo = %s"
            valor = (email.lower(), legajo)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 8:

            cursos_idCurso = input(
                "Ingrese el número del curso que pertenece (1-6): ").strip()
            while not cursos_idCurso.isdigit() or int(cursos_idCurso) < 1 or int(cursos_idCurso) > 6:
                print(c.rojo +"El número de curso debe ser entre 1 y 6."+ c.quit)
                cursos_idCurso = input("Ingrese el número del curso que pertenece (1-6): ").strip()

            sql = "UPDATE alumnos SET cursos_idCurso = %s WHERE legajo = %s"
            valor = (cursos_idCurso, legajo)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

    except Exception as e:
        print(c.rojo +f"Error al modificar los datos: {e}"+ c.quit)
    finally:
        cursor.close()
        conexion.close()

# -----> Modificación un dato en específico del profesor <------


def modificarProfesorEspecifico():
    listaProfesores()
    try:
        conexion_instancia = Conexion()
        conexion = conexion_instancia.conexionBD()
        cursor = conexion.cursor()

        # Solicitar el id del profesor que se desea modificar
        idProfesor = input("Ingrese el ID del Profesor que desea modificar: ")

        select = "SELECT * FROM profesores WHERE idProfesor = %s"
        cursor.execute(select, (idProfesor,))
        # Obtiene solo el primer registro de la consulta como tuplas
        resultado = cursor.fetchone()

        if not resultado:
            print(c.amarillo +"No se encontró un profesor con el ID proporcionado."+ c.quit)
            return
        os.system("cls")
        print("Datos actuales del profesor:")
        print(f"\n[1] . Nombre: {resultado[1]}\n[2] . Apellido: {resultado[2]}\n[3] . Teléfono: {resultado[3]}")
        print(f"[4] . Email: {resultado[4]}\n[5] . DNI: {resultado[5]}\n[6] . Fecha de Nacimiento: {resultado[6]}")
        print(f"[7] . Matrícula: {resultado[7]}\n[8] . Dirección: {resultado[8]}\n[9] . Horas: {resultado[9]}\n[10] . Sueldo: {resultado[10]}")
        # Solicita que dato quiero modificar
        menu = int(input("¿Qué dato desea modificar? :"))
        if menu == 1:

            nombre = input("Ingrese el nombre del profesor: ").strip()
            while not nombre.isalpha() or len(nombre) < 2:
                print(c.rojo +"Por favor, solo ingrese caracteres."+ c.quit)
                nombre = input("Ingrese el nombre del profesor: ").strip()

            sql = "UPDATE profesores SET Nombre = %s WHERE idProfesor = %s"
            valor = (nombre.title(), idProfesor)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 2:

            apellido = input("Ingrese el apellido del profesor: ").strip()
            while not apellido.isalpha() or len(apellido) < 2:
                print(c.rojo +"Por favor, solo ingrese caracteres."+ c.quit)
                apellido = input("Ingrese el apellido del profesor: ").strip()

            sql = "UPDATE profesores SET apellido = %s WHERE idProfesor = %s"
            valor = (apellido.title(), idProfesor)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 3:

            telefono = input("Ingrese el apellido del profesor: ").strip()
            if len(telefono) != 10 or not telefono.isdigit():
                while (len(telefono) != 10 or not telefono.isdigit()):
                    print(c.rojo +"El telefono debe contener 10 digitos."+ c.quit)
                    telefono = input("Ingrese el apellido del profesor: ").strip()

            sql = "UPDATE profesores SET telefono = %s WHERE idProfesor = %s"
            valor = (telefono, idProfesor)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 4:

            emailValido = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$' 
            while True:
                email = input("Ingrese el email del alumno: ").strip().lower() # lower convierte todas las letras del string en minúscula
                if re.match(emailValido, email): # verifica que el correo ingresado sea válido utilizando la librería re
                    break  # si el correo ingresado es válido pasa
                else:
                    print(c.rojo +"Ingrese un correo electrónico que sea válido."+ c.quit)

            sql = "UPDATE profesores SET email = %s WHERE idProfesor = %s"
            valor = (email.lower(), idProfesor)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 5:

            dni = input("Ingrese el DNI del profesor: ").strip()
            if len(dni) != 8 or not dni.isdigit():
                while (len(dni) != 8 or not dni.isdigit()):
                    print(c.rojo +"El DNI debe contener 8 digitos."+ c.quit)
                    dni = input("Ingrese el DNI del profesor: ").strip()
            sql = "UPDATE profesores SET dni = %s WHERE idProfesor = %s"
            valor = (dni, idProfesor)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 6:

            # Ingreso de la fecha de nacimiento del profesor
            # Ingreso de año
            print("Ingrese la fecha de nacimiento (YYYY-MM-DD) del profesor:\n")
            año = input("Ingrese el año (entre 1950 y 2004): ").strip()
            while not año.isdigit() or not (1950 <= int(año) <= 2004):
                print(c.rojo +"Por favor, ingrese un número válido entre 1950 y 2004."+ c.quit)
                año = input("Ingrese el año (entre 1950 y 2004): ").strip()
            # Ingreso de mes
            mes = input("Ingrese el mes: ").strip()
            while not mes.isdigit() or not (1 <= int(mes) <= 12):
                print(c.rojo +"Por favor, ingrese un número válido entre 1 y 12."+ c.quit)
                mes = input("Ingrese el mes: ").strip()
            # Ingreso de día
            dia = input("Ingrese el día: ").strip()
            while not dia.isdigit() or not (1 <= int(dia) <= 31):
                print(c.rojo +"Por favor, ingrese un número válido entre 1 y 31."+ c.quit)
                dia = input("Ingrese el día: ")

            fechaNacimiento = año + "-" + mes+ "-" + dia

            sql = "UPDATE profesores SET fechaNacimiento = %s WHERE idProfesor = %s"
            valor = (fechaNacimiento, idProfesor)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 7:

            matricula = input("Ingrese la matrícula del profesor: ")
            while not matricula.isalnum():
                print(c.rojo +"Por favor, sólo ingresar caracteres alfanumérico."+ c.quit)
                matricula = input(
                    "Ingrese la matrícula del profesor: ").strip()

            sql = "UPDATE profesores SET matricula = %s WHERE idProfesor = %s"
            valor = (matricula, idProfesor)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 8:

            direccion = input("Ingrese la dirección del profesor: ").strip()
            while len(direccion) < 3 or direccion.isdigit():
                if direccion.isdigit():
                    print(c.rojo +"Por favor, ingrese una dirección válida."+ c.quit)
                    direccion = input("Ingrese la dirección del profesor: ").strip()

            sql = "UPDATE profesores SET direccion = %s WHERE idProfesor = %s"
            valor = (direccion.title(), idProfesor)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 9:

            horas = input("Ingrese las horas del profesor: ").strip()
            if len(dni) < 1 or not dni.isdigit():
                while (len(dni) < 1 or not dni.isdigit()):
                    print(c.rojo +"Las horas no pueden ser menores a 1."+ c.quit)
                    dni = input("Ingrese las horas del profesor: ").strip()

            sql = "UPDATE profesores SET horas = %s WHERE idProfesor = %s"
            valor = (horas, idProfesor)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

        elif menu == 10:

            sueldo = input("Ingrese el sueldo del profesor: $").strip()
            while not sueldo.isdigit() or int(sueldo) <= 200000:
                print(c.rojo +"El sueldo debe ser un número mayor a $200000."+ c.quit)
                sueldo = input("Ingrese el sueldo del profesor: $").strip()

            sql = "UPDATE profesores SET sueldo = %s WHERE idProfesor = %s"
            valor = (sueldo, idProfesor)
            cursor.execute(sql, (valor))
            conexion.commit()

            print(c.verde +"Los datos fueron actualizados correctamente."+ c.quit)

    except Exception as e:
        print(c.rojo +f"Error al modificar los datos: {e}"+ c.quit)
    finally:
        cursor.close()
        conexion.close()

# ------------------- MUESTRA DE DATOS -------------------

# -------------------> Lista de alumnos completa <-------------------


def mostrarDatosAlumnos():
    try:
        conexion_instancia = Conexion()  # Crear una instancia de la conexión
        # Obtengo la conexión a la base de datos
        conexion = conexion_instancia.conexionBD()
        if not conexion:
            print(c.rojo +"Error: No se pudo conectar a la base de datos."+ c.quit)
            return

        cursor = conexion.cursor()  # Creo el cursor
        consulta = "SELECT legajo, nombre, apellido, dni, direccion, genero, fechaNacimiento, email, cursos_idCurso FROM escuela_privada.alumnos"
        # Ejecutar la consulta con el parámetro seguro (con tuplas y no como caracteres)
        cursor.execute(consulta)
        alumnos = cursor.fetchall()  # Obtiene todos los registros de la consulta como tuplas

        print("Datos de los alumnos:\n")
        for legajo, nombre, apellido, dni, direccion, genero, fechaNacimiento, email, cursos_idCurso in alumnos:
            print(f"Legajo: {legajo}, Nombre: {nombre}, Apellido: {apellido}, DNI: {dni}, Dirección: {direccion}, Género: {genero}, Fecha de nacimiento: {fechaNacimiento}, Email: {email}, Curso: {cursos_idCurso}")
            print("-"*200)
    except Exception as e:  # Muestra cual fue el error para que el programa no termine
        print(c.rojo +f"Ocurrió un error durante la consulta: {e}"+ c.quit)
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexión

# -------------------> Lista de alumnos ordenados alfabéticamente por apellido <-------------------


def mostrarAlumnosOrdenados():
    try:
        conexion_instancia = Conexion()  # Crear una instancia de la conexión
        conexion = conexion_instancia.conexionBD() # Obtengo la conexión a la base de dato
        if not conexion:
            print(c.rojo +"Error: No se pudo conectar a la base de datos."+ c.quit)
            return

        cursor = conexion.cursor()  # Creo el cursor
        consulta = """
            SELECT apellido, nombre, dni, legajo, direccion, cursos_idCurso
            FROM escuela_privada.alumnos 
            ORDER BY apellido ASC
        """
        cursor.execute(
            consulta)  # Ejecutar la consulta con el parámetro seguro (con tuplas y no como caracteres)
        alumnos = cursor.fetchall()  # Obtiene todos los registros de la consulta como tuplas
        print("Alumnos ordenados alfabéticamente por apellido:\n")
        for apellido, nombre, dni, legajo, direccion, cursos_idCurso in alumnos:
            print(
                f"Apellido: {apellido} , Nombre: {nombre}, DNI: {dni}, Legajo: {legajo}, Dirección: {direccion}, Curso: {cursos_idCurso}")
            print("-"*200)
    except Exception as e:  # Muestra cuál fue el error para que el programa no termine
        print(c.rojo +f"Ocurrió un error durante la consulta: {e}"+ c.quit)
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexión

# -------------------> Lista de profesores completa <-------------------


def mostrarDatosProfesores():
    try:
        conexion_instancia = Conexion()
        conexion = conexion_instancia.conexionBD()
        if not conexion:
            print(c.rojo +"Error: No se pudo conectar a la base de datos."+ c.quit)
            return

        cursor = conexion.cursor()
        consulta = "SELECT idProfesor, nombre, apellido, telefono, email, dni, fechaNacimiento, matricula, direccion, horas, sueldo FROM escuela_privada.profesores"
        cursor.execute(consulta)
        profesores = cursor.fetchall()
        print("Datos de los profesores:\n")
        for idProfesor, nombre, apellido, telefono, email, dni, fechaNacimiento, matricula, direccion, horas, sueldo in profesores:
            print(f"ID: {idProfesor}, Nombre: {nombre}, Apellido: {apellido}, Teléfono: {telefono}, Email: {email}, DNI: {dni}, Fecha de nacimiento: {fechaNacimiento}, Matrícula: {matricula}, Dirección: {direccion}, Horas: {horas}, Sueldo: ${sueldo}")
            print("-"*200)
    except Exception as e:
        print(c.rojo +f"Ocurrió un error durante la consulta: {e}"+ c.quit)
    finally:
        cursor.close()
        conexion.close()

# -------------------> Lista de alumnos ordenados alfabéticamente por apellido <-------------------


def mostrarProfesoresOrdenados():
    try:
        conexion_instancia = Conexion()  # Creo una instancia de la conexión
        # Obtengo la conexión a la base de datos
        conexion = conexion_instancia.conexionBD()
        if not conexion:
            print(c.rojo +"Error: No se pudo conectar a la base de datos."+ c.quit)
            return

        cursor = conexion.cursor()  # Creo el cursor
        consulta = """
            SELECT apellido, nombre, dni, matricula, telefono, direccion
            FROM escuela_privada.profesores 
            ORDER BY apellido ASC
        """
        cursor.execute(consulta) # Obtiene todos los registros de la consulta como tuplas no modificables
        profesores = cursor.fetchall()
        print("Profesores ordenados alfabéticamente por apellido:\n")
        for apellido, nombre, dni, matricula, telefono, direccion in profesores:
            print(
                f"Apellido: {apellido}, Nombre: {nombre}, DNI: {dni}, Matrícula: {matricula}, Teléfono: {telefono}, Dirección: {direccion}")
            print("-"*200)
    except Exception as e:
        print(c.rojo +f"Ocurrió un error durante la consulta: {e}"+ c.quit)
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexión

# ------------------- FILTRO DE BÚSQUEDA -------------------

# -------------------> Filtro para profesor especifico <-------------------

# Función para buscar a un alumno en específico


def buscarEspecificoProfesor(dato, comandoSQL):
    conexion_instacia = Conexion()  # Creo una instancia de la conexión
    conexion = conexion_instacia.conexionBD() # Obtengo la conexión a la base de datos

    # Si conexión es vacío o nada entra a la validación
    if (conexion is None):
        print(c.rojo +"Error: No se pudo establecer conexión con la base de datos."+ c.quit)
        return

    # Utilizamos un manejo de excepciones
    try:
        cursor = conexion.cursor()  # Creo el cursor
        # instruccion sql
        # f-strings permite insertar los valores de las variables dentro de la cadena directamente, de forma legible.
        query = f"SELECT idProfesor, nombre, apellido, telefono, email, dni, matricula, direccion, horas, sueldo FROM escuela_privada.profesores WHERE {comandoSQL}= %s"
        # Ejecutar la consulta con el parámetro seguro (con tuplas (no modificables) y no como caracteres)
        cursor.execute(query, (dato,))
        # Obtiene todos los registros de la consulta como tuplas no modificables
        resultados = cursor.fetchall()

        if (resultados):  # Muestro el encontrado
            os.system("cls")
            print("Datos encontrados.")
            for idProfesor, nombre, apellido, telefono, email, dni, matricula, direccion, horas, sueldo in resultados:
                print(f"Legajo: {idProfesor}, Nombre: {nombre}, Apellido: {apellido}, DNI: {dni}, Matrícula: {matricula}, Teléfono: {telefono}, Email: {email}, Dirección: {direccion}, Horas: {horas}, Sueldo: {sueldo}")
        else:
            print(c.amarillo +f"No se encontraron registros con: {dato}"+ c.quit)

    except Exception as e:  # Muestra cuál fue el error para que el programa no termine
        print(c.rojo +f"Ocurrió un error durante la consulta: {e}"+ c.quit)
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexión

# -------------------> Filtro para alumno específico <-------------------


def buscarEspecificoAlumnos(dato, comandoSQL):
    conexion_instancia = Conexion()  # Creo una instancia de la conexión
    # Obtengo la conexión a la base de datos
    conexion = conexion_instancia.conexionBD()

    # Si conexión es vacío o nada entra a la validación
    if (conexion is None):
        print(c.rojo +"Error: No se pudo establecer conexión con la base de datos."+ c.quit)
        return

    # Utilizamos un manejo de excepciones
    try:
        print(dato)
        cursor = conexion.cursor()  # Crear un cursor
        query = f"SELECT legajo, nombre, apellido, email, direccion, genero FROM escuela_privada.alumnos WHERE {comandoSQL} = %s"
        # Ejecutar la consulta con el parámetro seguro (con tuplas y no como caracteres)
        cursor.execute(query, (dato,))
        # Obtiene todos los registros de la consulta como tuplas no modificables
        resultados = cursor.fetchall()

        if resultados:
            os.system("cls")
            print("Datos encontrados:")
            for legajo, nombre, apellido, email, direccion, genero in resultados:
                # f-strings permite insertar los valores de las variables dentro de la cadena directamente, de forma legible.
                print(
                    f"Legajo: {legajo}, Nombre: {nombre}, Apellido: {apellido}, Email: {email}, Dirección: {direccion}, Género: {genero}")
        else:
            print(c.amarillo +f"No se encontraron registros con: {dato}"+ c.quit)

    except Exception as e:  # Muestra cuál fue el error para que el programa no termine
        print(c.rojo +f"Ocurrió un error durante la consulta: {e}"+ c.quit)
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexión

# -------------------> Lista corta de alumnos <-------------------


def listaAlumnos():
    try:
        conexion_instancia = Conexion()  # Crear una instancia de la conexión
        # Obtener la conexión a la base de datos
        conexion = conexion_instancia.conexionBD()
        cursor = conexion.cursor()  # Creo cursor

        sql = "SELECT legajo, apellido, nombre FROM alumnos ORDER BY legajo ASC"
        cursor.execute(sql)
        # Obtiene todos los registros de la consulta como tuplas no modificables
        resultado = cursor.fetchall()
        if not resultado:
            print(c.amarillo +"No hay alumnos registrados."+ c.quit)
            return

        print("Listado de alumnos")
        for alumnos in resultado:
            print(
                f"Legajo: {alumnos[0]}, Apellido: {alumnos[1]}, nombre: {alumnos[2]}")

            print("-"*150)

    except Exception as e:
        print(c.rojo +f"Ocurrió un error durante la consulta: {e}"+ c.quit)
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexion

# -------------------> Lista corta de profesores <-------------------


def listaProfesores():
    try:
        conexion_instancia = Conexion()  # Crear una instancia de la conexión
        # Obtener la conexión a la base de datos
        conexion = conexion_instancia.conexionBD()
        cursor = conexion.cursor()  # Creo cursor

        sql = "SELECT idprofesor, apellido, nombre FROM profesores ORDER BY idprofesor ASC"
        cursor.execute(sql)
        # Obtiene todos los registros de la consulta como tuplas no modificables
        resultado = cursor.fetchall()
        if not resultado:
            print(c.amarillo +"No hay profesores registrados."+ c.quit)
            return

        print("Listado de profesores")
        for profesor in resultado:
            print(f"Legajo: {profesor[0]}, Apellido: {profesor[1]}, nombre: {profesor[2]}")
            print("-"*150)

    except Exception as e:
        print(c.rojo +f"Ocurrió un error durante la consulta: {e}"+ c.quit)
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexion

# ------------------- ELIMINACIONES -------------------

# ------------> Bajas de alumnos <-------------------


def eliminarAlumno(dato):
    conexion_instancia = Conexion()  # Crear una instancia de la conexión
    # Obtener la conexión a la base de datos
    conexion = conexion_instancia.conexionBD()
    # Si no hay conexión con la base de datos
    if conexion is None:
        print(c.rojo +"Error: No se pudo establecer conexión con la base de datos."+ c.quit)
        return

    try:
        cursor = conexion.cursor()  # Creo cursor
        query = "DELETE FROM alumnos WHERE legajo = %s"
        cursor.execute(query, (dato,))
        conexion.commit()
        os.system("cls")
        print(c.verde +"Alumno eliminado exitosamente."+ c.quit)
    except Exception as e:
        print(c.rojo +f"Ocurrió un error durante la consulta: {e}"+ c.quit)
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()   # Cerrar la conexion

# ------------> Bajas de profesores <-------------------


def eliminarProfe(dato):
    conexion_instancia = Conexion()  # Crear una instancia de la conexión
    # Obtener la conexión a la base de datos
    conexion = conexion_instancia.conexionBD()
    if conexion is None:
        print(c.rojo +"Error: No se pudo establecer conexión con la base de datos."+ c.quit)
        return

    try:
        cursor = conexion.cursor()  # Creo cursor
        # Instrucción para eliminar un profesor
        query = "DELETE FROM profesores WHERE idProfesor = %s"
        # Ejecutar la consulta con el parámetro seguro (con tuplas y no como caracteres)
        cursor.execute(query, (dato,))
        conexion.commit()  # Confirma los cambios en la base de datos
        os.system("cls")
        print(c.verde +"Profesor dado de baja exitosamente."+ c.quit)
    except Exception as e:  # Muestra cuál fue el error para que el programa no termine
        print(c.rojo +f"Ocurrió un error durante la consulta: {e}"+ c.quit)
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexión