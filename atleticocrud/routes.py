from flask import render_template
from atleticocrud import app, db
from atleticocrud.models import Country, League


@app.route("/")
def home():
    return render_template("base.html")