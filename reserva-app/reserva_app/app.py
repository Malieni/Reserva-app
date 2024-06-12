from flask import flask , render_templete

app = Flask("Reserva App")

@app.route("/")
def principal():
    return render_template("principal.html")