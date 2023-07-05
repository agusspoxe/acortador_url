# acortador_url

## Acortador de url "EQUIPO A"

Este proyecto busca ofrecer al cliente, un acortador de URL, como  herramienta web que reduce la longitud de una dirección de una página web, asignando un conjunto de números y caracteres aleatorios que redirigen a la misma página. El objetivo es reducir la longitud de una dirección web para que sea más fácil de compartir y recordar.

Para crear el acortador de URL "EQUIPO A" a nivel de programación, hemos empleado el lenguaje de Python, base de datos MySQL,Flask que es un framework.

El proceso para crear nuestro acortador de URL "EQUIPO A" implica los siguientes pasos:

1. Solicitar una URL larga del usuario. WEB FARE.PY
2. Conseguir un dominio corto.
3. Crear una base de datos. `DATE BASE.PY`
4. Hacer que redireccione.
5. Registrar enlaces cortos.

El proceso parte de un fichero que hemos llamado "escuchar" donde se realiza la solicitud de acortar() y recuperar().

Este intercambia información con la base de datos "equipo_A" donde se realiza el almacenamiento y busqueda de las URLS, tanto url_large y las url_short.
`almacenar()` y `buscar()`.

De igual forma hemos incorporado el fichero "webinterface" donde su función es:
captura datos(), no valido() y redirigir().

![Diagrama](/static/images/diagrama.png)
