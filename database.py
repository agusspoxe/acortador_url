import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

load_dotenv(override=True)

config = {
    "host": os.getenv("SERVER"),
    "port": os.getenv("PORT"),
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "db": os.getenv("DATABASE"),
    "raise_on_warnings": True,
}

def buscar(url_corta):
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
        if len(url_corta) == 5:
            cursor = cnx.cursor()
            consultilla_larga = cursor.execute(
                f"""SELECT url_large FROM equipo_a.urls WHERE url_short = "{url_corta}";"""
            )
            resultado_larga = cursor.fetchone()

            if resultado_larga is not None:
                url_larga = resultado_larga[0]

            cursor.close()
            cnx.close()

        return url_larga

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
        cursor = cnx.cursor()
        q_data_guardar = f"""INSERT INTO `equipo_a`.`urls` (`url_short`, `url_large`)
            VALUES ('{url_corta}', '{url_larga}');
            """
        cursor.execute(q_data_guardar)
        cnx.commit()

        cursor.close()
        cnx.close()
