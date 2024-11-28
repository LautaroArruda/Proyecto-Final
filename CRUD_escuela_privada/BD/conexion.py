import mysql.connector
from mysql.connector import Error

class Conexion:
    @staticmethod
    def conexionBD():
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="escuela_privada",
                port=3306
            )
            return conexion
        except Error as ex:
            print(f"Error al intentar la conexión: {ex}")
            return None
    