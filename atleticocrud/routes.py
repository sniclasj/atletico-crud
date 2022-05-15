from flask import render_template, request, redirect, url_for
from atleticocrud import app, db
from atleticocrud.models import Country, League, Club, Player


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/countries")
def countries():
    countries = list(Country.query.order_by(Country.country_name).all())
    return render_template("countries.html", countries=countries)


@app.route("/add_country", methods = ["GET", "POST"])
def add_country():
    if request.method == "POST":
        country = Country(country_name=request.form.get("country_name"))
        db.session.add(country)
        db.session.commit()
        return redirect(url_for("countries"))
    return render_template("add_country.html")


@app.route("/edit_country/<int:country_id>", methods = ["GET", "POST"])
def edit_country(country_id):
    return render_template("edit_country.html")