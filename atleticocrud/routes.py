from flask import render_template
from atleticocrud import app, db
from atleticocrud.models import Country, League, Club, Player


@app.route("/")
def home():
    return render_template("countries.html")


@app.route("/add_country", methods = ["GET", "POST"])
def add_country():
    return render_template("add_country.html")