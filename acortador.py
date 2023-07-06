import hashlib
import string

LONGITUD = 5

def acortar(url_arga):
    url_corta = generar_url_corta(url_larga)
    bbdd = BBDD()  # Instancia de la clase BBDD
    bbdd.guardar_url(url_corta, url_larga)

    return url_corta

def generar_url_corta(url_larga):
    # Generar un hash MD5 a partir de la URL larga
    md5_hash = hashlib.md5(url_larga.encode()).hexdigest()
    url_corta = md5_hash[:LONGITUD]

    return url_corta

def generar_url_corta(url, longitud):
    caracteres = string.ascii_letters + string.digits  # Letras y números
    cadena_hash = generar_cadena_hash(url, longitud)
    
    return f"https://equipo.a/{cadena_hash}"

def prueba():


    def recoger_url_larga():
        return input("introduce la url: ")

    url_larga = 'pepito.com?ilusion=huesitos'
    url_corta = generar_url_corta(url_larga)
    comprobar_url_corta()
    print(url_corta)


if __name__ == "__main__":
    prueba()
