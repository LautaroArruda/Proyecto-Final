from BD.conexion import Conexion
import os
import mysql.connector

def listaAlumnos():
    try:
        conexion = Conexion()
        cone = conexion.conexionBD()  # Usa el atributo `.conexion` de la clase Conexion
        cursor = cone.cursor()

        sql = "SELECT legajo, apellido, nombre FROM alumnos ORDER BY legajo ASC"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        if not resultado:
            print("No hay alumnos registrados.")
            return

        print("Listado de alumnos")
        for alumnos in resultado:
            print(
                f"Legajo: {alumnos[0]}, Apellido: {alumnos[1]}, nombre: {alumnos[2]}")

            print("-"*50)

    except mysql.connector.Error as error:
        print("Error al mostrar los datos Error: {}".format(error))
    finally:
        if cursor:
            cursor.close()
        if cone:
            cone.close()

def listaProfesores():
    try:
        conexion = Conexion()
        cone = conexion.conexionBD()  # Usa el atributo `.conexion` de la clase Conexion
        cursor = cone.cursor()

        sql = "SELECT idprofesor, apellido, nombre FROM profesores ORDER BY idprofesor ASC"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        if not resultado:
            print("No hay profesores registrados.")
            return

        print("Listado de profesores")
        for profesor in resultado:
            print(
                f"Legajo: {profesor[0]}, Apellido: {profesor[1]}, nombre: {profesor[2]}")

            print("-"*50)

    except mysql.connector.Error as error:
        print("Error al mostrar los datos Error: {}".format(error))
    finally:
        if cursor:
            cursor.close()
        if cone:
            cone.close()


def ingresarAlumnos():
    try:
        # Crear una instancia de la conexión
        conexion = Conexion()
        cone = conexion.conexionBD()  # Usa el atributo `.conexion` de la clase Conexion
        cursor = cone.cursor()

        # Ingreso de nombre del alumno
        nombre = input("Ingrese el nombre del alumno: ").strip()
        while not nombre.isalpha() or len(nombre) < 3:
            print("Por favor, solo ingrese caracteres.")
            nombre = input("Ingrese el nombre del alumno: ").strip()

        # Ingreso de apellido del alumno
        apellido = input("Ingrese el apellido del alumno: ").strip()
        while not apellido.isalpha() or len(apellido) < 3:
            print("Por favor, solo ingrese caracteres.")
            apellido = input("Ingrese el apellido del alumno: ").strip()

        # Ingreso de dni del alumno
        dni = input("Ingrese el DNI del alumno: ").strip()
        if len(dni) !=8 or not dni.isdigit():
            while(len(dni) !=8 or not dni.isdigit()):
                print("El DNI debe contener 8 digitos.")
                dni = input("Ingrese el dni del alumno: ").strip()

        # Ingreso de direccion del alumno
        direccion = input("Ingrese la dirección del alumno: ").strip()
        while len(direccion) < 3:
            print("Por favor, ingrese una direccion valida")
            direccion = input("Ingrese el dirección del Alumno: ").strip()

        # Ingreso de direccion del alumno
        opciones_validas = ["Masculino", "Femenino", "Transgenero", "No binario"]
        genero = input("Ingresar genero (masculino, femenino, transgenero y no binario): ").capitalize()
        while not genero.replace(" ", "").isalpha() or genero not in opciones_validas:
            print("Porfavor solo ingresar caracteres.")
            genero = input("Ingresar genero (masculino, femenino, transgenero y no binario): ").capitalize()

        # Ingreso de la fecha de nacimiento del alumno
        fechaNacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")

        # Ingreso del email del alumno
        email = input("Ingrese el email del Alumno: ").strip().lower()
        while "@" not in email:
            print("El correo electrónico no es válido. Debe contener un '@'.")
            email = input("Ingrese el email del Alumno: ").strip().lower()

        # Ingreso del curso del alumno
        cursos_idCurso = input("Ingrese el ID del curso al que pertenece (1-6): ")
        while not cursos_idCurso.isdigit() or int(cursos_idCurso) < 1 or int(cursos_idCurso) > 6:
            print("El ID del curso debe ser un número entre 1 y 6.")
            cursos_idCurso = input("Ingrese el ID del curso al que pertenece (1-6): ")

        # Consulta SQL para insertar datos
        sql = """INSERT INTO alumnos (nombre, apellido, dni, direccion, genero,
                 fechaNacimiento, email, cursos_idCurso)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = ( nombre.title(), apellido.title(), dni, direccion.title(),
                   genero, fechaNacimiento, email.lower(), cursos_idCurso)

        # Ejecutar la consulta
        cursor.execute(sql, valores)
        cone.commit()  # Confirmar los cambios en la base de datos
        # Limpiar la consola
        os.system("cls")
        print(f"{cursor.rowcount} registro(s) ingresado(s) exitosamente.")

        # Cerrar el cursor y la conexión
        cursor.close()
        cone.close()
    except mysql.connector.Error as error:
        print("Error al ingresar datos: {}".format(error))
    finally:
        if cursor:
            cursor.close()
        if cone:
            cone.close()


def ingresarProfesor():
    try:
        conexion = Conexion()
        cone = conexion.conexionBD()
        cursor = cone.cursor()
        # Solicitar datos del Profesor

        # Ingreso nombre del alumno
        nombre = input("Ingrese el nombre del Profesor: ").strip()
        while not nombre.isalpha() or len(nombre) < 3:
            print("Por favor, solo ingrese caracteres.")
            nombre = input("Ingrese el nombre del Profesor: ").strip()

        # Ingreso apellido del alumno
        apellido = input("Ingrese el apellido del Profesor: ").strip()
        while not apellido.isalpha() or len(apellido) < 3:
            print("Por favor, solo ingrese caracteres.")
            apellido = input("Ingrese el apellido del Profesor: ").strip()

        # Ingreso telefono del alumno
        telefono = input("Ingrese el telefono del Profesor: ").strip()
        if len(telefono) != 10 or not telefono.isdigit():
            while (len(telefono) != 10 or not telefono.isdigit()):
                print("El telefono debe contener 10 digitos.")
                telefono = input("Ingrese el telefono del profesor: ").strip()

        # Ingreso email del alumno
        email = input("Ingrese la email del Profesor: ").strip().lower()
        while "@" not in email:
            print("El correo electrónico no es válido. Debe contener un '@'.")
            email = input("Ingrese el email del profesor: ").strip().lower()

        # Ingreso dni del alumno
        dni = input("Ingrese el dni del Profesor: ").strip()
        if len(dni) !=8 or not dni.isdigit():
            while(len(dni) !=8 or not dni.isdigit()):
                print("El DNI debe contener 8 digitos.")
                dni = input("Ingrese el dni del Profesor: ").strip()

        fechaNacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")

        matricula = input("Ingrese el matricula del Profesor: ").strip()
        while not matricula.isalnum():
            print("Porfavor solo ingresar caracteres alfanumerico.")
            matricula = input("Ingresar matricula: ").strip()

        direccion = input("Ingrese la direccion del Profesor: ").strip()
        while len(direccion) < 3:
            print("Por favor, ingrese una direccion valida")
            direccion = input("Ingrese el nombre del Profesor: ").strip()

        horas = input("Ingrese las horas: ").strip()
        if len(dni) < 1 or not dni.isdigit():
            while(len(dni) < 1 or not dni.isdigit()):
                print("Las horas no pueden ser menor a 1.")
                dni = input("Ingrese las horas: ").strip()

        sueldo = input("Ingrese el sueldo del profesor: ").strip()
        while not sueldo.isdigit() or int(sueldo) <= 200000:
            print("El sueldo debe ser un número mayor a 200000.")
            sueldo = input("Ingrese el sueldo del profesor: ").strip()

        # Consulta SQL para insertar datos

        sql = """INSERT INTO profesores (nombre, apellido, telefono, email,
                   dni, fechaNacimiento, matricula, direccion, horas, sueldo)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"""
        valores = (nombre.title(), apellido.title(), telefono, email,
                   dni, fechaNacimiento, matricula, direccion.title(), horas, sueldo)  # idProfesor

        # Ejecutar la consulta
        cursor.execute(sql, valores)
        cone.commit()  # Confirmar los cambios en la base de datos
        # Limpiar la consola
        os.system("cls")
        print(f"{cursor.rowcount} registro(s) ingresado(s) exitosamente.")

        # Cerrar el cursor y la conexión
        cursor.close()
        cone.close()
    except mysql.connector.Error as error:
        print("Error al ingresar datos: {}".format(error))
    finally:
        if cursor:
            cursor.close()
        if cone:
            cone.close()


def modificarAlumno():
    listaAlumnos()
    try:
        # Conectar a la base de datos
        conexion = Conexion()
        cone = conexion.conexionBD()  # Usa el atributo `.conexion` de la clase Conexion
        cursor = cone.cursor()

        # Solicitar el legajo del alumno que se desea modificar
        legajo = input("Ingrese el legajo del alumno que desea modificar: ").strip()

        # Verificar si el alumno existe
        select = "SELECT * FROM alumnos WHERE legajo = %s"
        cursor.execute(select, (legajo,))
        # En Python, el método fetchone() se utiliza para devolver una sola fila de resultados de una consulta SQL
        resultado = cursor.fetchone()

        if not resultado:
            print("No se encontró un alumno con el legajo proporcionado.")
            return

        print("Datos actuales del alumno:")
        print(
            f"\nLegajo: {resultado[0]}\nNombre: {resultado[1]}\nApellido: {resultado[2]}\nDNI: {resultado[3]}")
        print(
            f"Dirección: {resultado[4]}\nGénero: {resultado[5]}\nFecha de Nacimiento: {resultado[6]}")
        print(f"Email: {resultado[7]}\nCurso ID: {resultado[8]}\n")

        # Solicitar nuevos datos
        print("\nIngrese los nuevos datos del alumno :")

        nlegajo = input("Legajo : ")

        nombre = input("Nombre : ").strip()
        while not nombre.isalpha() or len(nombre) < 3:
            print("Por favor, solo ingrese caracteres.")
            nombre = input("Ingrese el Nombre del Alumno: ").strip()

        apellido = input("Apellido : ").strip()
        while not apellido.isalpha() or len(apellido) < 3:
            print("Por favor, solo ingrese caracteres.")
            apellido = input("Ingrese el apellido del Alumno: ").strip()

        dni = input("DNI : ").strip()
        if len(dni) !=8 or not dni.isdigit():
            while(len(dni) !=8 or not dni.isdigit()):
                print("El DNI debe contener 8 digitos.")
                dni = input("Ingrese el dni del Alumno: ").strip()

        direccion = input("Dirección : ").strip()
        while len(direccion) < 3:
            print("Por favor, ingrese una direccion valida.")
            direccion = input("Direccion: ").strip()

        opciones_validas = ["Masculino", "Femenino", "Transgenero", "No binario"]
        genero = input("Género : ").strip()
        while not genero.replace(" ", "").isalpha() or genero not in opciones_validas:
            print("Porfavor solo ingresar caracteres.")
            genero = input("Ingresar genero (masculino, femenino, transgero y no binario): ").capitalize()

        fechaNacimiento = input("Fecha de Nacimiento (YYYY-MM-DD) : ")

        email = input("Email: ").strip().lower
        while "@" not in email:
            print("El email no es válido. Debe contener un '@'.")
            email = input("Ingrese el email del Alumno: ").strip().lower

        curso_id = input("Curso ID : ").strip()
        while not curso_id.isdigit() or int(curso_id) < 1 or int(curso_id) > 6:
            print("El ID del curso debe ser un número entre 1 y 6.")
            curso_id = input("Ingrese el ID del curso al que pertenece (1-6): ").strip()
        # Actualizar datos en la base de datos
        sql = """UPDATE alumnos
                        SET legajo = %s, nombre = %s, apellido = %s, dni = %s, direccion = %s, genero = %s,
                            fechaNacimiento = %s, email = %s, cursos_idCurso = %s
                        WHERE legajo = %s"""
        valores = (nlegajo, nombre.title(), apellido.title(), dni, direccion.title(), genero,
                   fechaNacimiento, email.lower(), curso_id, legajo)

        cursor.execute(sql, valores)
        cone.commit()

        print(
            "Datos del alumno  actualizados correctamente.")

        # Cerrar la conexión
        cursor.close()
        cone.close()

    except mysql.connector.Error as error:
        print(f"Error al modificar los datos: {error}")
    finally:
        if cursor:
            cursor.close()
        if cone:
            cone.close()


def modificarProfesor():
    listaProfesores()
    try:
        # Conectar a la base de datos
        conexion = Conexion()
        cone = conexion.conexionBD()  # Usa el atributo `.conexion` de la clase Conexion
        cursor = cone.cursor()

        # Solicitar el legajo del alumno que se desea modificar
        idProfesor = input("Ingrese el Id del Profesor que desea modificar: ").strip()

        # Verificar si el alumno existe
        select = "SELECT * FROM profesores WHERE idProfesor = %s"
        cursor.execute(select, (idProfesor,))
        # En Python, el método fetchone() se utiliza para devolver una sola fila de resultados de una consulta SQL
        resultado = cursor.fetchone()

        if not resultado:
            print("No se encontró un profesor con el id proporcionado.")
            return

        print("Datos actuales del profesor:")
        print(
            f"\nidProfesor: {resultado[0]}\nNombre: {resultado[1]}\nApellido: {resultado[2]}\nTelefono: {resultado[3]}")
        print(
            f"Email: {resultado[4]}\nDni: {resultado[5]}\nFecha de Nacimiento: {resultado[6]}")
        print(
            f"Matricula: {resultado[7]}\nDireccion: {resultado[8]}\nHoras: {resultado[9]}\nSueldo: {resultado[10]}")

        # Solicitar nuevos datos
        print("\nIngrese los nuevos datos del profesor:")

        nombre = input("Ingrese el nombre del Profesor: ").strip()
        while not nombre.isalpha() or len(nombre) < 3:
            print("Por favor, solo ingrese caracteres.")
            nombre = input("Ingrese el nombre del Profesor: ").strip()

        apellido = input("Ingrese el apellido del Profesor: ").strip()
        while not apellido.isalpha() or len(apellido) < 3:
            print("Por favor, solo ingrese caracteres.")
            apellido = input("Ingrese el apellido del Profesor: ").strip()

        telefono = input("Ingrese el telefono del Profesor: ").strip()
        if len(telefono) != 10 or not telefono.isdigit():
            while (len(telefono) != 10 or not telefono.isdigit()):
                print("El telefono debe contener 10 digitos.")
                telefono = input("Ingrese el telefono del profesor: ").strip()

        email = input("Ingrese la email del Profesor: ").strip().lower
        while "@" not in email:
            print("El correo electrónico no es válido. Debe contener un '@'.")
            email = input("Ingrese el correo electrónico del profesor: ").strip().lower

        dni = input("Ingrese el dni del Profesor: ").strip()
        if len(dni) !=8 or not dni.isdigit():
            while(len(dni) !=8 or not dni.isdigit()):
                print("El DNI debe contener 8 digitos.")
                dni = input("Ingrese el dni del Profesor: ").strip()

        fechaNacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")

        matricula = input("Ingrese el matricula del Profesor: ")
        while not dato.isalnum():
            print("Porfavor solo ingresar caracteres alfanumerico.")
            dato = input("Ingresar matricula: ").strip()

        direccion = input("Ingrese la direccion del Profesor: ").strip()
        while len(direccion) < 3:
            print("Por favor, ingrese una direccion valida.")
            direccion = input("Ingrese el nombre del Profesor: ").strip()

        horas = input("Ingrese las horas: ").strip()

        sueldo = input("Ingrese el sueldo: ").strip()
        while not sueldo.isdigit() or int(sueldo) <= 200000:
            print("El sueldo debe ser un número mayor a 200000.")
            sueldo = input("Ingrese el sueldo del profesor: ").strip()

        # Actualizar datos en la base de datos
        sql = """UPDATE profesores SET nombre = %s, apellido = %s, telefono = %s, email = %s, dni = %s, fechaNacimiento = %s, matricula = %s, direccion = %s , horas = %s ,sueldo = %s  WHERE idProfesor = %s """
        valores = (nombre.title(), apellido.title(), telefono, email.lower(), dni,
                   fechaNacimiento, matricula, direccion.title(), horas, sueldo, idProfesor)

        cursor.execute(sql, valores)
        cone.commit()

        print("Datos del profesor actualizados correctamente.")

        # Cerrar la conexión
        cursor.close()
        cone.close()

    except mysql.connector.Error as error:
        print(f"Error al modificar los datos: {error}")
    finally:
        if cursor:
            cursor.close()
        if cone:
            cone.close()


def modificarAlumnoEspecifico():

    listaAlumnos()
    try:
        # Conectar a la base de datos
        conexion = Conexion()
        cone = conexion.conexionBD()
        cursor = cone.cursor()

        # Solicitar el legajo del alumno que se desea modificar
        legajo = input("Ingrese el legajo del alumno que desea modificar: ")

        select = "SELECT * FROM alumnos WHERE legajo = %s"
        cursor.execute(select, (legajo,))
        resultado = cursor.fetchone()

        if not resultado:
            print("No se encontró un alumno con el legajo proporcionado.")
            return
        # Limpiar la consola
        os.system("cls")
        print("Datos actuales del alumno:")
        print(
            f"\n[1] . Nombre: {resultado[0]}\n[2] . Apellido: {resultado[1]}\n[3] . DNI: {resultado[2]}")
        print(
            f"[4] . Dirección: {resultado[3]}\n[5] . Género: {resultado[4]}\n[6] . Fecha de Nacimiento: {resultado[5]}")
        print(f"[7] . Email: {resultado[6]}\n[8] . Curso ID: {resultado[7]}\n")

        # menu

        menu = int(input("¿Qué dato desea modificar?: ").strip())
        if menu == 1:

            nombre = input("Nombre: ").strip()
            while not nombre.isalpha() or len(nombre) < 3:
                print("Por favor, solo ingrese caracteres.")
                nombre = input("Ingrese el nombre del Alumno: ").strip()
            
            sql = "UPDATE alumnos SET Nombre = %s WHERE legajo = %s"
            valor = (nombre.title(), legajo)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 2:

            apellido = input("Apellido: ").strip()
            while not apellido.isalpha() or len(apellido) < 3:
                print("Por favor, solo ingrese caracteres.")
                apellido = input("Ingrese el apellido del Alumno: ").strip()

            sql = "UPDATE alumnos SET apellido = %s WHERE legajo = %s"
            valor = (apellido.title(), legajo)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 3:

            dni = input("DNI: ").strip()
            if len(dni) !=8 or not dni.isdigit():
                while(len(dni) !=8 or not dni.isdigit()):
                    print("El DNI debe contener 8 digitos.")
                    dni = input("Ingrese el dni del Alumno: ").strip()

            sql = "UPDATE alumnos SET dni = %s WHERE legajo = %s"
            valor = (dni, legajo)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 4:

            direccion = input("Direccion: ").strip()
            while len(direccion) < 3:
                print("Por favor, solo ingrese caracteres.")
                direccion = input("Direccion: ").strip()
            sql = "UPDATE alumnos SET direccion = %s WHERE legajo = %s"
            valor = (direccion.title(), legajo)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 5:
            opciones_validas = ["Masculino", "Femenino", "Transgenero", "No binario"]
            genero = input("Genero: ")
            while not genero.replace(" ", "").isalpha() or genero not in opciones_validas:
                print("Porfavor solo ingresar caracteres.")
                genero = input("Ingresar genero (masculino, femenino, transgero y no binario): ").capitalize()
            sql = "UPDATE alumnos SET genero = %s WHERE legajo = %s"
            valor = (genero, legajo)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 6:

            fechaNacimiento = input("Fecha de  nacimiento: ")

            sql = "UPDATE alumnos SET fechaNacimiento = %s WHERE legajo = %s"
            valor = (fechaNacimiento, legajo)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 7:

            email = input("Email: ").strip().lower()
            while "@" not in email:
                print("El correo electrónico no es válido. Debe contener un '@'.")
                email = input("Ingrese el correo electrónico del profesor: ").strip().lower()

            sql = "UPDATE alumnos SET email = %s WHERE legajo = %s"
            valor = (email.lower(), legajo)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 8:

            cursos_idCurso = input("Curso ID: ").strip()
            while not cursos_idCurso.isdigit() or int(cursos_idCurso) < 1 or int(cursos_idCurso) > 6:
                print("El ID del curso debe ser un número entre 1 y 6.")
                cursos_idCurso = input("Ingrese el ID del curso al que pertenece (1-6): ").strip()

            sql = "UPDATE alumnos SET cursos_idCurso = %s WHERE legajo = %s"
            valor = (cursos_idCurso, legajo)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

    except mysql.connector.Error as error:
        print(f"Error al modificar los datos: {error}")
    finally:
        if cursor:
            cursor.close()
        if cone:
            cone.close()


def modificarProfesorEspecifico():

    listaProfesores()
    try:
        # Conectar a la base de datos
        conexion = Conexion()
        cone = conexion.conexionBD()
        cursor = cone.cursor()

        # Solicitar el legajo del profesor que se desea modificar
        idProfesor = input(
            "Ingrese el id del Profesor que desea modificar: ")

        select = "SELECT * FROM profesores WHERE idProfesor = %s"
        cursor.execute(select, (idProfesor,))
        resultado = cursor.fetchone()

        if not resultado:
            print("No se encontró un alumno con el legajo proporcionado.")
            return
        # Limpiar la consola
        os.system("cls")
        print("Datos actuales del profesor:")
        print(
            f"\n[1] . Nombre: {resultado[1]}\n[2] . Apellido: {resultado[2]}\n[3] . Telefono: {resultado[3]}")
        print(
            f"[4] . Email: {resultado[4]}\n[5] . Dni: {resultado[5]}\n[6] . Fecha de Nacimiento: {resultado[6]}")
        print(
            f"[7] . Matricula: {resultado[7]}\n[8] . Direccion: {resultado[8]}\n[9] . Horas: {resultado[9]}\n[10] . Sueldo: {resultado[10]}")

        # menu

        menu = int(input("¿Qué dato desea modificar? :"))
        if menu == 1:

            nombre = input("Nombre: ").strip()
            while not nombre.isalpha() or len(nombre) < 3:
                print("Por favor, solo ingrese caracteres.")
                nombre = input("Ingrese el nombre del Profesor: ").strip()

            sql = "UPDATE profesores SET Nombre = %s WHERE idProfesor = %s"
            valor = (nombre.title(), idProfesor)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 2:

            apellido = input("Apellido: ").strip()
            while not apellido.isalpha() or len(apellido) < 3:
                print("Por favor, solo ingrese caracteres.")
                apellido = input("Ingrese el apellido del Profesor: ").strip()

            sql = "UPDATE profesores SET apellido = %s WHERE idProfesor = %s"
            valor = (apellido.title(), idProfesor)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 3:

            telefono = input("Telefono: ").strip()
            if len(telefono) != 10 or not telefono.isdigit():
                while (len(telefono) != 10 or not telefono.isdigit()):
                    print("El telefono debe contener 10 digitos.")
                    telefono = input("Ingrese el telefono del profesor: ").strip()

            sql = "UPDATE profesores SET telefono = %s WHERE idProfesor = %s"
            valor = (telefono, idProfesor)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 4:

            email = input("Email: ").strip().lower()
            while "@" not in email:
                print("El correo electrónico no es válido. Debe contener un '@'.")
                email = input("Ingrese el correo electrónico del profesor: ").strip().lower()

            sql = "UPDATE profesores SET email = %s WHERE idProfesor = %s"
            valor = (email.lower(), idProfesor)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 5:

            dni = input("Dni: ").strip()
            if len(dni) !=8 or not dni.isdigit():
                while(len(dni) !=8 or not dni.isdigit()):
                    print("El DNI debe contener 8 digitos.")
                    dni = input("Ingrese el dni del Profesor: ").strip()
            sql = "UPDATE profesores SET dni = %s WHERE idProfesor = %s"
            valor = (dni, idProfesor)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 6:

            fechaNacimiento = input("Fecha de  nacimiento: ")

            sql = "UPDATE profesores SET fechaNacimiento = %s WHERE idProfesor = %s"
            valor = (fechaNacimiento, idProfesor)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 7:

            matricula = input("Matricula: ")
            while not dato.isalnum():
                print("Porfavor solo ingresar caracteres alfanumerico.")
                dato = input("Ingresar matricula").strip()

            sql = "UPDATE profesores SET matricula = %s WHERE idProfesor = %s"
            valor = (matricula, idProfesor)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 8:

            direccion = input("Direccion: ").strip()
            while len(direccion) < 3:
                print("Por favor, ingresar una direccion valida.")
                direccion = input("Direccion: ").strip()
            sql = "UPDATE profesores SET direccion = %s WHERE idProfesor = %s"
            valor = (direccion.title(), idProfesor)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 9:

            horas = input("Horas: ")

            sql = "UPDATE profesores SET horas = %s WHERE idProfesor = %s"
            valor = (horas, idProfesor)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

        elif menu == 10:

            sueldo = input("Sueldo: ").strip()
            while not sueldo.isdigit() or int(sueldo) <= 200000:
                print("El sueldo debe ser un número mayor a 200000.")
                sueldo = input("Ingrese el sueldo del profesor: ").strip()

            sql = "UPDATE profesores SET sueldo = %s WHERE idProfesor = %s"
            valor = (sueldo, idProfesor)
            cursor.execute(sql, (valor))
            cone.commit()

            print("datos actualizado correctamente.")

    except mysql.connector.Error as error:
        print(f"Error al modificar los datos: {error}")
    finally:
        if cursor:
            cursor.close()
        if cone:
            cone.close()
# Funcion para buscar a un alumno en especifico
def buscarEspecificoProfesor(dato, comandoSQL):
    conexion_instacia = Conexion() #Creo una instancia de la conexión
    conexion = conexion_instacia.conexionBD() #Crear una instancia de la conexión

    # si conexion es vacio o nada entra a la validacion
    if (conexion is None):
        print("Error: No se pudo establecer conexión con la base de datos.")
        return
    
    #Utilizamos un manejo de ecepciones
    try:
        cursor = conexion.cursor() #Creo el cursor
        #instruccion sql
        query = f"SELECT idProfesor, nombre, apellido, telefono, email, dni, matricula, direccion, horas, sueldo FROM escuela_privada.profesores WHERE {comandoSQL}= %s"# f-strings permite insertar los valores de las variables dentro de la cadena directamente, de forma legible.
        cursor.execute(query, (dato,)) # Ejecutar la consulta con el parámetro seguro (con tuplas(no mificables) y no como caracteres)
        resultados = cursor.fetchall()

        if(resultados):#Mustro el encontrado
            # Limpiar la consola
            os.system("cls")
            print("Datos encontrados.")
            for idProfesor, nombre, apellido, telefono, email, dni, matricula, direccion, horas, sueldo in resultados:
                print(f"Legajo: {idProfesor}, Nombre: {nombre}, Apellido: {apellido}, DNI: {dni}, Matricula: {matricula}, Telefono: {telefono}, Email: {email}, Direccion: {direccion}, Horas: {horas}, Sueldo: {sueldo}") 
        else:
            print(f"No se encontraron registros con: {dato}")
            
    except Exception as e:
        print(f"Ocurrió un error durante la consulta: {e}")
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexión
# Funcion para buscar a un alumno en especifico
def buscarEspecificoAlumnos(dato, comandoSQL):
    conexion_instancia = Conexion()  #Creo una instancia de la conexión
    conexion = conexion_instancia.conexionBD() #Obtengo la conexión a la base de datos

    # si conexion es vacio o nada entra a la validacion
    if (conexion is None):
        print("Error: No se pudo establecer conexión con la base de datos.")
        return
    
    #Utilizamos un manejo de ecepciones
    try:
        print(dato)
        cursor = conexion.cursor()  # Crear un cursor
        query = f"SELECT legajo, nombre, apellido, email, direccion, genero FROM escuela_privada.alumnos WHERE {comandoSQL} = %s"
        cursor.execute(query, (dato,))  # Ejecutar la consulta con el parámetro seguro (con tuplas y no como caracteres)
        resultados = cursor.fetchall()  # Obtener todos los registros encontrados tuplas


        if resultados:
            # Limpiar la consola
            os.system("cls")
            print("Datos encontrados:")
            for legajo, nombre, apellido, email, direccion, genero in resultados:
                print(f"Legajo: {legajo}, Nombre: {nombre}, Apellido: {apellido}, Email: {email}, Direccion: {direccion}, Genero: {genero}")# f-strings permite insertar los valores de las variables dentro de la cadena directamente, de forma legible.
        else:
            print(f"No se encontraron registros con: {dato}")
        
    except Exception as e:
        print(f"Ocurrió un error durante la consulta: {e}")
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexión
# Funcion mostrar profesores
def motrarProfes():
    conexion_instancia = Conexion()  # Crear una instancia de la conexión
    conexion = conexion_instancia.conexionBD()
    try:
        cursor = conexion.cursor()
        query = "SELECT idProfesor, nombre, apellido, matricula FROM profesores"
        cursor.execute(query)
        alumno = cursor.fetchall()
        if alumno:
            for legajo, nombre, apellido, matricula  in alumno:
                print(f"ID: {legajo} Nombre: {nombre} Apellido: {apellido} Matricula: {matricula} ")
    except Exception as e:
        print(f"Ocurrió un error durante la consulta: {e}")
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexión
# Funcion mostrar alumnos
def motrarAlumnos():
    conexion_instancia = Conexion()  # Crear una instancia de la conexión
    conexion = conexion_instancia.conexionBD()
    try:
        cursor = conexion.cursor()
        query = "SELECT legajo,nombre,apellido FROM alumnos"
        cursor.execute(query)
        alumno = cursor.fetchall()
        if alumno:
            for legajo, nombre, apellido in alumno:
                print(f"Legajo: {legajo} Nombre: {nombre} Apellido: {apellido} ")
    except Exception as e:
        print(f"Ocurrió un error durante la consulta: {e}")
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexión
# Funcion eliminar alumno
def eliminarAlumno(dato):
    conexion_instancia = Conexion()  # Crear una instancia de la conexion
    conexion = conexion_instancia.conexionBD() # Obtener la conexion a la base de datos
    # Si no hay conexcion con la BD
    if conexion is None:
        print("Error: No se pudo establecer conexión con la base de datos.")
        return
    
    try:  
        cursor = conexion.cursor() # Creo cursor
        query = "DELETE FROM alumnos WHERE legajo = %s" #Intruccion para eliminar un alumno
        cursor.execute(query, (dato,))         
        conexion.commit() # Confirmo los cambios en la BD
        os.system("cls")
        print("Alumno eliminado exitosamente.")   
    except Exception as e:
        print(f"Ocurrio un error durante la consulta: {e}")
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexion
# Funcion eliminar profesor
def eliminarProfe(dato):
    conexion_instancia = Conexion()  # Crear una instancia de la conexion
    conexion = conexion_instancia.conexionBD() # Obtener la conexion a la base de datos
    if conexion is None:
        print("Error: No se pudo establecer conexión con la base de datos.")
        return
    
    try:  
        cursor = conexion.cursor()
        query = "DELETE FROM profesores WHERE idProfesor = %s" #Intruccion para eliminar un profe
        cursor.execute(query, (dato,))         
        conexion.commit() # Confirmo los cambios en la BD 
        os.system("cls")
        print("Porfesor dado de baja exitosamente.")   
    except Exception as e:
        print(f"Ocurrio un error durante la consulta: {e}")
    finally:
        cursor.close()  # Cerrar el cursor
        conexion.close()  # Cerrar la conexion


