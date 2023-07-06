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

1-url_short :primary key+NN chaps(5)
2-url_large: NN+ varchar(2048)
3-creation_date now()
`almacenar()` y `buscar()`.


De igual forma hemos incorporado el fichero "webinterface" donde su función es:
captura datos(), no valido() y redirigir().

El proyecto busca ofrecer al cliente una estética mejorada; Un acortador de URL que permite transformar enlaces largos y complicados en URL cortas y limpias. Esto mejora la apariencia visual de los enlaces, lo que resulta más atractivo y profesional para los usuarios.
Dentro de nuestros servicio podremos devolver al cliente de acuerdo a sus necesidades, tanto la url_short y la url_large en su origen; teniendo la posibilidad de guardar ambas urls en nuestra Base de Datos "equipo A"

![Diagrama](/static/images/diagrama.png)
