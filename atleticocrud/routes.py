from flask import render_template
from atleticocrud import app, db
from atleticocrud.models import Country, League, Club, Player


@app.route("/")
def home():
    return render_template("countries.html")


@app.route("/add_country", methods = ["GET", "POST"])
def add_country():
    if request.method == "POST":
        country = Country(country_name=request.form.get("country_name"))
        db.session.add(country)
        db.session.commit
        return redirect(url_for("countries"))
    return render_template("add_country.html")