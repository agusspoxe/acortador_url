from flask import Flask, render_template, request, url_for, flash, redirect
from random import randint

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=("GET", "POST"))
def index():
    return render_template("index.html")


@app.route("/escuchar_url_larga", methods=["POST"])
def action():
    url_larga = request.json["url_larga"]
    # url_corta = acortar(url_larga)
    codigo = "P" + randint(0000, 9999).__str__().zfill(4)
    # url_corta = "http://localhost:8000/" + codigo
    url_corta = "http://equipo.a/" + codigo

    return {"respuesta": url_corta}


# run the application
if __name__ == "__main__":
    app.run(port=8000, debug=True)
