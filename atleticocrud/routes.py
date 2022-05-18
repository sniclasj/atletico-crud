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
    country = Country.query.get_or_404(country_id)
    if request.method == "POST":
        country.country_name = request.form.get("country_name")
        db.session.commit()
        return redirect(url_for("countries"))
    return render_template("edit_country.html", country=country)
 

@app.route("/delete_country/<int:country_id>")
def delete_country(country_id):
    country = Country.query.get_or_404(country_id)
    db.session.delete(country)
    db.session.commit()
    return redirect(url_for("countries"))


@app.route("/leagues/<int:country_id>")
def leagues(country_id):
    leagues = list(League.query.order_by(League.id).filter(League.country_id==country_id))
    return render_template("leagues.html", leagues=leagues)


@app.route("/add_league", methods = ["GET", "POST"])
def add_league():
    countries = list(Country.query.order_by(Country.country_name).all())
    if request.method == "POST":
        league = League(
            league_name=request.form.get("league_name"),
            country_id=request.form.get("country_id")
            )
        db.session.add(league)
        db.session.commit()
        return redirect(url_for("leagues", country_id=league.country_id))
    return render_template("add_league.html", countries=countries)


@app.route("/edit_league/<int:league_id>", methods = ["GET", "POST"])
def edit_league(league_id):
    league = League.query.get_or_404(league_id)
    if request.method == "POST":
        league.league_name = request.form.get("league_name")
        db.session.commit()
        return redirect(url_for("leagues", country_id=league.country_id))
    return render_template("edit_league.html", league=league)


@app.route("/delete_league/<int:league_id>")
def delete_league(league_id):
    league = League.query.get_or_404(league_id)
    db.session.delete(league)
    db.session.commit()
    return redirect(url_for("leagues", country_id=league.country_id))


@app.route("/clubs/<int:league_id>")
def clubs(league_id):
    clubs = list(Club.query.order_by(Club.club_name).filter(Club.league_id==league_id))
    return render_template("clubs.html", clubs=clubs)


@app.route("/add_club", methods = ["GET", "POST"])
def add_club():
    leagues = list(League.query.order_by(League.league_name).all())
    if request.method == "POST":
        club = Club(
            club_name=request.form.get("club_name"),
            league_id=request.form.get("league_id")
            )
        db.session.add(club)
        db.session.commit()
        return redirect(url_for("clubs", league_id=club.league_id))
    return render_template("add_club.html", leagues=leagues)


@app.route("/edit_club/<int:club_id>", methods = ["GET", "POST"])
def edit_club(club_id):
    club = Club.query.get_or_404(club_id)
    if request.method == "POST":
        club.club_name = request.form.get("club_name")
        db.session.commit()
        return redirect(url_for("clubs", league_id=club.league_id))
    return render_template("edit_club.html", club=club)


@app.route("/delete_club/<int:club_id>")
def delete_club(club_id):
    club = Club.query.get_or_404(club_id)
    db.session.delete(club)
    db.session.commit()
    return redirect(url_for("clubs", league_id=club.league_id))