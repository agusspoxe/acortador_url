from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=("GET", "POST"))
def index():
    return render_template("index.html")


@app.route("/action", methods=["POST"])
def action():
    red = request.form.get("red")
    print("POST HRRRERRR")

    return {"respuesta": "brrrrrrrr"}

    # return render_template('action.html', red=red)


# run the application
if __name__ == "__main__":
    app.run(debug=True)
