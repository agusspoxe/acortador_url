import hashlib
from database import buscar

class Escuchar:
    def acortar(self):
        url_larga = input("Ingrese la URL larga: ")
        url_corta = self.generar_url_corta(url_larga)
        bbdd = BBDD()  # Instancia de la clase BBDD
        bbdd.guardar_url(url_corta, url_larga)
        return url_corta

    def generar_url_corta(self, url_larga):
        # Generar un hash MD5 a partir de la URL larga
        md5_hash = hashlib.md5(url_larga.encode()).hexdigest()
        url_corta = md5_hash[:5]
        return url_corta

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
