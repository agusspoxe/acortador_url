# import random
# import string

# url_larga = input("introduce la url: ")
# print(url_larga)


# def generar_cadena_aleatoria(longitud):
#     caracteres = string.ascii_letters + string.digits  # Letras y números
#     cadena_aleatoria = "".join(random.choice(caracteres) for _ in range(longitud))
#     return cadena_aleatoria


# longitud_deseada = 5  # Longitud de la cadena aleatoria
# cadena_aleatoria = generar_cadena_aleatoria(longitud_deseada)
# print(f"equipoa.com//{cadena_aleatoria}")


# Python3 code for above approach
# def idToShortURL(id):
#     map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#     shortURL = ""

#     # for each digit find the base 62
#     while id > 0:
#         shortURL += map[id % 62]
#         id //= 62

#     # reversing the shortURL
#     return shortURL[len(shortURL) :: -1]


# def shortURLToId(shortURL):
#     id = 0
#     for i in shortURL:
#         val_i = ord(i)
#         if val_i >= ord("a") and val_i <= ord("z"):
#             id = id * 62 + val_i - ord("a")
#         elif val_i >= ord("A") and val_i <= ord("Z"):
#             id = id * 62 + val_i - ord("A") + 26
#         else:
#             id = id * 62 + val_i -  ord("0") + 52
#     return id


# if __name__ == "__main__":
#     id = 12345
#     shortURL = idToShortURL(id)
#     print("Short URL from 12345 is : ", shortURL)
#     print("ID from", shortURL, "is : ", shortURLToId(shortURL))
# ·······················································································
# import hashlib
# import string

# LONGITUD = 5

# url = [
#     "https://www.amazon.es/dp/B0BBRZ6JB2/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B0BBRZ6JB2&pd_rd_w=T5JMa&content-id=amzn1.sym.9c67f205-18e7-4d34-beb2-37ec708092ed&pf_rd_p=9c67f205-18e7-4d34-beb2-37ec708092ed&pf_rd_r=YKYCH5PDK8H20YF0Y2PH&pd_rd_wg=sLFg2&pd_rd_r=3227b502-e6c4-4443-b5c7-c7ddeab6d3e0&s=toys&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw",
#     "http://www.google.es/",
#     "http://www.google.esoipfjosipdjfosddeee/",
#     "http://www.google.xn--esfjisjdoajfjdsfaojoasjpd-ioc/",
# ]
# cantidad = len(url)
# print(cantidad)


# def recoger_url_larga():
#     return input("introduce la url: ")


# def comprobar_url_laga():
#     pass


# def comprobar_url_corta():
#     pass


# def generar_cadena_hash(url, longitud=5):
#     hash = hashlib.sha1(url.encode("UTF-8")).hexdigest()
#     print(hash)

#     return hash[:longitud]


# def generar_url_corta(url, longitud):
#     caracteres = string.ascii_letters + string.digits  # Letras y números
#     cadena_hash = generar_cadena_hash(url, longitud)

#     return f"https://equipo.a/%7Bcadena_hash%7D"


# def main():
#     url = recoger_url_larga()
#     comprobar_url_laga()
#     url_corta = generar_url_corta(url, LONGITUD)
#     comprobar_url_corta()
#     print(url_corta)


# if __name__ == "__main__":
#     main()
# ············································································
# class BBDD:
#     def recuperar_url_larga(self, url_corta):
#         # Lógica para recuperar la URL larga de la base de datos
#         # Aquí puedes implementar tu propia lógica de acceso a la base de datos
#         # y retornar la URL larga correspondiente
#         return "https://www.ejemplo.com"


# class Servidor:
#     def capturar_datos(self, url_larga):
#         # Lógica para capturar datos de la URL larga
#         # Aquí puedes implementar tu propia lógica para capturar los datos
#         # correspondientes a la URL larga y retornar la información capturada
#         return "no_valida"


# class Escuchar:
#     def __init__(self):
#         self.bbdd = BBDD()
#         self.servidor = Servidor()

#     def recibir_url_corta(self, url_corta):
#         url_larga = self.bbdd.recuperar_url_larga(url_corta)
#         datos = self.servidor.capturar_datos(url_larga)
#         return datos


# # Ejemplo de uso
# escuchar = Escuchar()
# url_corta = "https://shorturl"
# datos = escuchar.recibir_url_corta(url_corta)
# print("Datos obtenidos:", datos)


# ·······················································································
# class Escuchar:
#     def idToShortURL(id):
#         map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#         shortURL = ""

#         while id > 0:
#             shortURL += map[id % 62]
#             id //= 62

#         return shortURL[::-1]

#     def shortURLToId(shortURL):
#         id = 0
#         for i in shortURL[::-1]:
#             val_i = ord(i)
#             if val_i >= ord("a") and val_i <= ord("z"):
#                 id = id * 62 + val_i - ord("a")
#             elif val_i >= ord("A") and val_i <= ord("Z"):
#                 id = id * 62 + val_i - ord("A") + 26
#             else:
#                 id = id * 62 + val_i - ord("0") + 52
#         return id

#     def main(self):
#         id = 12345
#         shortURL = self.idToShortURL(id)
#         print("Short URL from 12345 is:", shortURL)
#         print("ID from", shortURL, "is:", self.shortURLToId(shortURL))


# if __name__ == "__main__":
#     escuchar = Escuchar()
#     escuchar.main()


# class BaseDeDatos(Escuchar):
#     def recuperar_url_larga(self, url_corta):
#         pass


# class Servidor(Escuchar):
#     def capturar_datos(self, url_larga):
#         pass
# ·······················································································

import hashlib


class Escuchar:
    def acortar(self):
        url_larga = input("Ingrese la URL larga: ")
        url_corta = self.generar_url_corta(url_larga)
        return url_corta

    def generar_url_corta(self, url_larga):
        # Generar un hash MD5 a partir de la URL larga
        md5_hash = hashlib.md5(url_larga.encode()).hexdigest()
        url_corta = md5_hash[:5]
        return url_corta

    def recuperar(self):
        bbdd = BBDD()  # Instancia de la clase BBDD
        url_corta = input("Ingrese la URL corta: ")
        url_larga = bbdd.recuperar_url_larga(url_corta)
        return url_larga


escuchar = Escuchar()
url_corta = escuchar.acortar()
print("URL corta:", url_corta)


class BBDD:
    def recuperar_url_larga(self, url_corta):
        # Lógica para recuperar la URL larga de la base de datos
        # Aquí tenemos que implementar la logica para que nos de la url larga
        # y retornar la URL larga correspondiente
        return url_larga


# ·······················································································
