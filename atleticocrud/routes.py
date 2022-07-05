from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from atleticocrud import app, db, mongo
from atleticocrud.models import Country, League, Club, Users


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = Users.query.filter(
            Users.user_name == request.form.get("username").lower()).all()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        user = Users(
            user_name=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
            )

        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = Users.query.filter(
            Users.user_name == request.form.get("username").lower()).all()

        if existing_user:
            print(request.form.get("username"))
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user[0].password, request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    if "user" in session:
        return render_template("profile.html", username=session["user"])

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("Log Out Successful!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/countries")
def countries():
    countries = list(Country.query.order_by(Country.country_name).all())
    return render_template("countries.html", countries=countries)


@app.route("/add_country", methods=["GET", "POST"])
def add_country():
    if session["user"] != "admin":
        return redirect(url_for("countries"))
    else:
        if request.method == "POST":
            country = Country(
                country_name=request.form.get("country_name"),
                country_image_url=request.form.get("country_image_url")
            )
            db.session.add(country)
            db.session.commit()
            return redirect(url_for("countries"))
        return render_template("add_country.html")


@app.route("/edit_country/<int:country_id>", methods=["GET", "POST"])
def edit_country(country_id):
    country = Country.query.get_or_404(country_id)
    if request.method == "POST":
        country.country_name = request.form.get("country_name")
        country.country_image_url = request.form.get("country_image_url")
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
    if country_id == 0:
        leagues = list(League.query.order_by(League.league_name).all())
        return render_template("leagues.html", leagues=leagues)
    else:
        leagues = list(League.query.order_by(League.id).filter(
            League.country_id == country_id))
        return render_template("leagues.html", leagues=leagues)


@app.route("/add_league", methods=["GET", "POST"])
def add_league():
    if session["user"] != "admin":
        return redirect(url_for("leagues", country_id=0))
    else:
        countries = list(Country.query.order_by(Country.country_name).all())
        if request.method == "POST":
            league = League(
                league_name=request.form.get("league_name"),
                league_image_url=request.form.get("league_image_url"),
                country_id=request.form.get("country_id")
                )
            db.session.add(league)
            db.session.commit()
            return redirect(url_for("leagues", country_id=league.country_id))
        return render_template("add_league.html", countries=countries)


@app.route("/edit_league/<int:league_id>", methods=["GET", "POST"])
def edit_league(league_id):
    league = League.query.get_or_404(league_id)
    if request.method == "POST":
        league.league_name = request.form.get("league_name")
        league.league_image_url = request.form.get("league_image_url")
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
    if league_id == 0:
        clubs = list(Club.query.order_by(Club.club_name).all())
        return render_template("clubs.html", clubs=clubs)
    else:
        clubs = list(Club.query.order_by(Club.club_name).filter(
            Club.league_id == league_id))
        return render_template("clubs.html", clubs=clubs)


@app.route("/add_club", methods=["GET", "POST"])
def add_club():
    if session["user"] != "admin":
        return redirect(url_for("clubs", league_id=0))
    else:
        leagues = list(League.query.order_by(League.league_name).all())
        if request.method == "POST":
            club = Club(
                club_name=request.form.get("club_name"),
                club_image_url=request.form.get("club_image_url"),
                league_id=request.form.get("league_id")
                )
            db.session.add(club)
            db.session.commit()
            return redirect(url_for("clubs", league_id=club.league_id))
        return render_template("add_club.html", leagues=leagues)


@app.route("/edit_club/<int:club_id>", methods=["GET", "POST"])
def edit_club(club_id):
    club = Club.query.get_or_404(club_id)
    if request.method == "POST":
        club.club_name = request.form.get("club_name")
        club.club_image_url = request.form.get("club_image_url")
        db.session.commit()
        return redirect(url_for("clubs", league_id=club.league_id))
    return render_template("edit_club.html", club=club)


@app.route("/delete_club/<int:club_id>")
def delete_club(club_id):
    club = Club.query.get_or_404(club_id)
    db.session.delete(club)
    db.session.commit()
    return redirect(url_for("clubs", league_id=club.league_id))


@app.route("/playersa/<club_id>")
def playersa(club_id):
    if club_id == "0":
        playersa = mongo.db.players.find()
        return render_template("playersa.html", playersa=playersa)
    else:
        playersa = mongo.db.players.find({"club_id": club_id})
        return render_template("playersa.html", playersa=playersa)


@app.route("/add_playera", methods=["GET", "POST"])
def add_playera():
    if session["user"] != "admin":
        return redirect(url_for("playersa", club_id=0))
    else:
        if request.method == "POST":
            new_playera = request.form.get("club_id")
            if mongo.db.players.count_documents(
                    {"club_id": new_playera}, limit=40) == 0:
                club = Club.query.get_or_404(request.form.get("club_id"))
                playersa = {
                    "name": request.form.get("player_name"),
                    "dob": request.form.get("player_dob"),
                    "nationality": request.form.get(
                        "player_nationality"),
                    "position": request.form.get("player_position"),
                    "club_id": request.form.get("club_id"),
                    "image_url": request.form.get("player_image_url")
                }
                mongo.db.players.insert_one(playersa)
                return redirect(url_for("playersa", club_id=club.id))
            else:
                flash("This player already has stats")
                return redirect(url_for("add_playera"))

        clubs = list(Club.query.order_by(Club.club_name).all())
        return render_template("add_playera.html", clubs=clubs)


@app.route("/edit_playera/<player_id>", methods=["GET", "POST"])
def edit_playera(player_id):
    if session["user"] != "admin":
        return redirect(url_for("playersa", club_id=0))
    else:
        player = mongo.db.players.find_one({"_id": ObjectId(player_id)})
        if request.method == "POST":
            submit = {
                "name": request.form.get("player_name"),
                "dob": request.form.get("player_dob"),
                "nationality": request.form.get(
                    "player_nationality"),
                "position": request.form.get("player_position"),
                "club_id": request.form.get("club_id"),
                "image_url": request.form.get("player_image_url")
                }
            mongo.db.player.find_one_and_update({"_id": ObjectId(player_id)}, submit)
            flash("Player Updated!")
        return render_template("edit_playera.html", player=player)
