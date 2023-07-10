import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, flash, redirect
from random import randint
from acortador import generar_url_corta
from database import almacenar
from database import buscar

load_dotenv()

config = {
    'host': os.getenv('SERVER'),
    'portweb': os.getenv('PORTWEB')

}
 

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=("GET", "POST"))
def index():
    return render_template("index.html")


@app.route("/404", methods=("GET", "POST"))
def error():
    return render_template("error.html")


@app.route("/escuchar_url_larga", methods=["POST"])
def action():
    url_larga = request.json["url_larga"]
    codigo = generar_url_corta(url_larga)
    almacenar(codigo, url_larga)
    url_corta = f'{config["host"]}:{config["portweb"]}/{codigo}'

    # url_corta = "http://equipo.a/" + codigo

    return {"respuesta": url_corta}


@app.route("/<string:codigo>", methods=["GET"])
def redirigir(codigo):
    print(codigo)
    url_larga = buscar(codigo)
    print(url_larga)
    return redirect(url_larga, code=302)
    # return redirect("http://www.example.com", code=302)

# run the application
if __name__ == "__main__":
    app.run(port=8000, debug=True, host="0.0.0.0")
