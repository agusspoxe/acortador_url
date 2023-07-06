import hashlib
from acortador import generar_url_corta
from database import buscar
from webinterface import action

class Escuchar:



    def recuperar(self):
        bbdd = BBDD()  # Instancia de la clase BBDD
        url_larga = bbdd.recuperar_url_larga(url_corta)
        return url_larga


class BBDD:
    def __init__(self):
        self.data = (
            {}
        )  # Almacena las URL cortas como claves y las URL largas como valores

    def guardar_url(self, url_corta, url_larga):
        self.data[url_corta] = url_larga

    def recuperar_url_larga(self, url_corta):
        if url_corta in self.data:
            return self.data[url_corta]
        else:
            return None

url_larga = action()
print(url_larga)
url_corta = generar_url_corta('https://www.amazon.es/')
# print
# escuchar = Escuchar()
# url_corta = escuchar.acortar()
# print(url_corta)
# print(f"URL corta: https://equipoa.com/{url_corta}")
url_corta_javier = f"URL corta: https://equipoa.com/{url_corta}"
print(url_corta_javier)
