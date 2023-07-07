import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

# import main

load_dotenv(override=True)

config = {
    "host": os.getenv("SERVER"),
    "port": os.getenv("PORT"),
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "db": os.getenv("DATABASE"),
    "raise_on_warnings": True,
}


def buscar():
    try:
        cnx = mysql.connector.connect(**config)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo está mal con el nombre de usuario o contraseña")
            print(err)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)

    else:
        url_corta = input("dame url corta: ")
        if len(url_corta) == 5:
            cursor = cnx.cursor()
            consultilla_larga = cursor.execute(
                f"""SELECT url_large FROM equipo_a.urls WHERE url_short = "{url_corta}";"""
            )
            resultado_larga = cursor.fetchone()

            if resultado_larga is not None:
                url_larga = resultado_larga[0]
                print(url_larga)
                print(f"la url larga de {url_corta} es {resultado_larga[0]}")
            else:
                print("ESTA URL NO EXISTE")
                # almacenar(url_corta)
            cursor.close()
            cnx.close()
        else:
            print("URL NO VÁLIDA!!! LISTILLO")


def almacenar(url_corta, url_larga):
    try:
        cnx = mysql.connector.connect(**config)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo está mal con el nombre de usuario o contraseña")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)

    else:
        # url_corta = input("dame url corta: ")

        # url_larga = input("dame url larga: ")

        cursor = cnx.cursor()
        q_data_guardar = f"""INSERT INTO `equipo_a`.`urls` (`url_short`, `url_large`)
            VALUES ('{url_corta}', '{url_larga}');
            """
        cursor.execute(q_data_guardar)
        cnx.commit()

        cursor.close()
        cnx.close()


if __name__ == "__main__":
    # almacenar()
    buscar()
    # url_larga= input("dame url larga: ")
    # almacenar('1234c',url_larga)


# def demo():
#     try:
#         cnx = mysql.connector.connect(**config)

#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Algo está mal con el nombre de usuario o contraseña")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("La base de datos no existe")
#         else:
#             print(err)

#     else:
#         print("aqui meteremos el sql")

#         cursor = cnx.cursor()
#         consultilla_corta = cursor.execute("""SELECT url_short FROM equipo_a.urls;""")
#         print(cursor)
#         resultado_corta = cursor.fetchone()

#         print(f"Hay {len(resultado_corta)} resultados cortos")
#         for resultado in resultado_corta:
#             print(f"url cortita como yo..: {resultado}")

#         consultilla_larga = cursor.execute("""SELECT url_large FROM equipo_a.urls;""")
#         resultado_larga = cursor.fetchone()

#         print(f"Hay {len(resultado_larga)} resultados largos")
#         for resultado in resultado_larga:
#             print(f"url larguita como turutu..: {resultado}")

#         cnx.close()


# try:
#     connection = mysql.connector.connect(
#         host = 'localhost',
#         port = 3306,
#         user = 'root',
#         password = 'OjoCuidao',
#         db = 'equipo_a'

#     )

#     if connection.is_connected():
#         print('conexion buena')
#         info_servidor = connection.get_server_info()
#         print(f"informacion server: {info_servidor}")
#         cursor = connection.cursor()
#         print(f"cursor {cursor}")
#         cursor.execute("SELECT DATABASE()")
#         # cursor.exectue("SELECT * FROM equipo_a")
#         row = cursor.fetchone()
#         print(f"conectado a la base de datos {row}")

# except Exception as ex:
#     print(ex)
############################################################################


# resultado_larga = cursor.te

# with cnx.cursor() as cursor:
#     # listamos las urls que tenemos
#     consultilla = cursor.execute("""
#     SELECT
#         url_short
#     FROM equipo_a.urls;
#     """)

#     urls = {}
#     for (url_corta) in cursor:
#         urls[]

# print(consultilla)
#   with cnx.cursor() as cursor:
#     # Consulta para obtener todas las aulas y sus profesores
#     cursor.execute("""
#     SELECT a.id, a.nombre, u.nombre, u.apellido, u.correo
#     FROM aulas a
#     INNER JOIN aulas_profesores ap ON a.id = ap.aula_id
#     INNER JOIN profesores p ON ap.profesor_id = p.usuario_id
#     INNER JOIN usuarios u ON p.usuario_id = u.id;
#     """)


#         # Mapeamos el resultado en un diccionario para fácil acceso
#         aulas = {}
#         for (id_aula, nombre_aula, nombre_prof, apellido_prof, correo_prof) in cursor:
#             aulas[id_aula] = {
#                 'nombre': nombre_aula, 'profesor': f'{nombre_prof} {apellido_prof} ({correo_prof})', 'alumnos': []}

#         # Consulta para obtener todos los alumnos y a qué aula están asignados
#         cursor.execute("""
#         SELECT a.id, u.nombre, u.apellido, u.correo
#         FROM aulas a
#         INNER JOIN aulas_alumnos aa ON a.id = aa.aula_id
#         INNER JOIN alumnos al ON aa.alumno_id = al.usuario_id
#         INNER JOIN usuarios u ON al.usuario_id = u.id;
#         """)

#         for (id_aula, nombre_alumno, apellido_alumno, correo_alumno) in cursor:
#             aulas[id_aula]['alumnos'].append(
#                 f'{nombre_alumno} {apellido_alumno} ({correo_alumno})')

#     # Imprimimos el informe
#     for id_aula, aula in aulas.items():
#         print(f"Aula ID: {id_aula}")
#         print(f"Nombre del Aula: {aula['nombre']}")
#         print(f"Profesor Asignado: {aula['profesor']}")
#         print("Alumnos:")
#         for alumno in aula['alumnos']:
#             print(f"  - {alumno}")
#         print("\n")
