import random
import string

url_larga = input("introduce la url: ")
print(url_larga)


def generar_cadena_aleatoria(longitud):
    caracteres = string.ascii_letters + string.digits  # Letras y números
    cadena_aleatoria = "".join(random.choice(caracteres) for _ in range(longitud))
    return cadena_aleatoria


longitud_deseada = 5  # Longitud de la cadena aleatoria
cadena_aleatoria = generar_cadena_aleatoria(longitud_deseada)
print(cadena_aleatoria)
