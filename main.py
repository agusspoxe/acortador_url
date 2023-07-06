import hashlib
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


escuchar = Escuchar()
url_corta = escuchar.acortar()
print(url_corta)
print(f"URL corta: https://equipoa.com/{url_corta}")
url_corta_javier = f"URL corta: https://equipoa.com/{url_corta}"
