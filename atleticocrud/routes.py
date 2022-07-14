from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func
from atleticocrud import app, db, mongo
from atleticocrud.models import Country, League, Club, Users


# Route for homepage for registration/log-in
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
            flash("Username Already Exists!")
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
            Users.user_name == request.form.get("username").lower()).first()

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user.password, request.form.get("password")):  # noqa
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


# Route for all countries
@app.route("/countries")
def countries():
    countries = list(Country.query.order_by(Country.country_name).all())
    return render_template("countries.html", countries=countries)


# Route to add a country if admin
@app.route("/add_country", methods=["GET", "POST"])
def add_country():
    if session["user"] != "admin":
        return redirect(url_for("countries"))

    if request.method == "POST":

        existing_country = Country.query.filter(
            func.lower(Country.country_name) == request.form.get(
                "country_name").lower()).first()
        if existing_country:
            flash("Country Already Exists!")
            return redirect(url_for("add_country"))

        country = Country(
            country_name=request.form.get("country_name"),
            country_image_url=request.form.get("country_image_url")
            )

        db.session.add(country)
        db.session.commit()
        flash("Country Successfully Added!")
        return redirect(url_for("countries"))

    return render_template("add_country.html")


# Route to edit country if admin
@app.route("/edit_country/<int:country_id>", methods=["GET", "POST"])
def edit_country(country_id):
    country = Country.query.get_or_404(country_id)

    if request.method == "POST":

        existing_country = Country.query.filter(
            func.lower(Country.country_name) == request.form.get(
                "country_name").lower()).first()
        if existing_country:
            flash("Country Already Exists!")
            return redirect(url_for("countries"))

        country.country_name = request.form.get("country_name")
        country.country_image_url = request.form.get("country_image_url")
        db.session.commit()
        flash("Country Successfully Updated!")
        return redirect(url_for("countries"))
    return render_template("edit_country.html", country=country)


# Route to delete country if admin
@app.route("/delete_country/<int:country_id>")
def delete_country(country_id):
    if session["user"] != "admin":
        return redirect(url_for("countries"))
    else:
        country = Country.query.get_or_404(country_id)
        mongo.db.players.delete_many({"country_id": (country_id)})
        db.session.delete(country)
        db.session.commit()
        flash("Country Successfully Deleted!")
        return redirect(url_for("countries"))


# Route to display all leagues if country_id == 0
# Otherwise route displays leagues for a specific country_id
@app.route("/leagues/<int:country_id>")
def leagues(country_id):
    if country_id == 0:
        leagues = list(League.query.order_by(League.league_name).all())
        return render_template("leagues.html", leagues=leagues)
    else:
        leagues = list(League.query.order_by(League.id).filter(
            League.country_id == country_id))
        return render_template("leagues.html", leagues=leagues)


# Route to add league if admin
@app.route("/add_league", methods=["GET", "POST"])
def add_league():
    if session["user"] != "admin":
        return redirect(url_for("leagues", country_id=0))

    countries = list(Country.query.order_by(Country.country_name).all())
    if request.method == "POST":
        existing_league = League.query.filter(
            func.lower(League.league_name) == request.form.get(
                "league_name").lower()).first()

        if existing_league:
            flash("League Already Exists!")
            return redirect(url_for("add_league"))

            league = League(
                league_name=request.form.get("league_name"),
                league_image_url=request.form.get("league_image_url"),
                country_id=request.form.get("country_id")
                )
            db.session.add(league)
            db.session.commit()
            flash("League Successfully Added!")
            return redirect(url_for(
                "leagues", country_id=league.country_id))
    return render_template("add_league.html", countries=countries)


# Route to edit league if admin
@app.route("/edit_league/<int:league_id>", methods=["GET", "POST"])
def edit_league(league_id):
    countries = list(Country.query.order_by(Country.country_name).all())
    league = League.query.get_or_404(league_id)
    if request.method == "POST":

        existing_league = League.query.filter(
            func.lower(League.league_name) == request.form.get(
                "league_name").lower()).first()

        if existing_league:
            flash("League Already Exists!")
            return redirect(url_for("leagues", country_id=0))

        league.league_name = request.form.get("league_name")
        league.league_image_url = request.form.get("league_image_url")
        league.country_id = request.form.get("country_id")
        db.session.commit()
        flash("League Successfully Updated!")
        return redirect(url_for("leagues", country_id=league.country_id))
    return render_template(
        "edit_league.html", league=league, countries=countries)


# Route to delete league if admin
@app.route("/delete_league/<int:league_id>")
def delete_league(league_id):
    if session["user"] != "admin":
        return redirect(url_for("leagues", country_id=0))
    else:
        league = League.query.get_or_404(league_id)
        mongo.db.players.delete_many({"league_id": (league_id)})
        db.session.delete(league)
        db.session.commit()
        flash("League Successfully Deleted!")
        return redirect(url_for("leagues", country_id=league.country_id))


# Route to display all clubs if league_id == 0
# Otherwise route displays clubs for a specific league_id
@app.route("/clubs/<int:league_id>")
def clubs(league_id):
    if league_id == 0:
        clubs = list(Club.query.order_by(Club.club_name).all())
        return render_template("clubs.html", clubs=clubs)
    else:
        clubs = list(Club.query.order_by(Club.club_name).filter(
            Club.league_id == league_id))
        return render_template("clubs.html", clubs=clubs)


# Route to add club if admin
@app.route("/add_club", methods=["GET", "POST"])
def add_club():
    if session["user"] != "admin":
        return redirect(url_for("clubs", league_id=0))

    leagues = list(League.query.order_by(League.league_name).all())
    if request.method == "POST":

        existing_club = Club.query.filter(
            func.lower(Club.club_name) == request.form.get(
                "club_name").lower()).first()

        if existing_club:
            flash("Club Already Exists!")
            return redirect(url_for("add_club"))

            club = Club(
                club_name=request.form.get("club_name"),
                club_image_url=request.form.get("club_image_url"),
                league_id=request.form.get("league_id")
                )
            db.session.add(club)
            db.session.commit()
            flash("Club Successfully Added!")
            return redirect(url_for("clubs", league_id=club.league_id))
    return render_template("add_club.html", leagues=leagues)


# Route to edit club if admin
@app.route("/edit_club/<int:club_id>", methods=["GET", "POST"])
def edit_club(club_id):
    leagues = list(League.query.order_by(League.league_name).all())
    club = Club.query.get_or_404(club_id)
    if request.method == "POST":
        club.club_name = request.form.get("club_name")
        club.club_image_url = request.form.get("club_image_url")
        club.league_id = request.form.get("league_id")
        db.session.commit()
        flash("Club Successfully Updated!")
        return redirect(url_for("clubs", league_id=club.league_id))
    return render_template("edit_club.html", club=club, leagues=leagues)


# Route to delete club if admin
@app.route("/delete_club/<club_id>")
def delete_club(club_id):
    if session["user"] != "admin":
        return redirect(url_for("clubs", league_id=0))
    else:
        club = Club.query.get_or_404(club_id)
        mongo.db.players.delete_many({"club_id": (club_id)})
        db.session.delete(club)
        db.session.commit()
        flash("Club Successfully Deleted!")
        return redirect(url_for("clubs", league_id=club.league_id))


# Route to display all players if league_id == 0
# Otherwise route displays players for a specific league_id
@app.route("/playersa/<club_id>")
def playersa(club_id):
    if club_id == "0":
        playersa = mongo.db.players.find()
        return render_template("playersa.html", playersa=playersa)
    else:
        playersa = mongo.db.players.find({"club_id": club_id})
        return render_template("playersa.html", playersa=playersa)


# Route to add player if admin
@app.route("/add_playera", methods=["GET", "POST"])
def add_playera():
    if session["user"] != "admin":
        return redirect(url_for("playersa", club_id=0))
    else:
        if request.method == "POST":
            new_playera = request.form.get("player_image_url")
            if mongo.db.players.count_documents(
                    {"image_url": new_playera}, limit=1) == 0:
                club = Club.query.get_or_404(request.form.get("club_id"))
                league = club.league_id
                get_league = League.query.get_or_404(league)
                country = get_league.country_id
                playersa = {
                    "name": request.form.get("player_name"),
                    "dob": request.form.get("player_dob"),
                    "nationality": request.form.get(
                        "player_nationality"),
                    "position": request.form.get("player_position"),
                    "club_id": request.form.get("club_id"),
                    "league_id": league,
                    "country_id": country,
                    "image_url": request.form.get("player_image_url")
                }
                mongo.db.players.insert_one(playersa)
                flash("Player Successfully Added!")
                return redirect(url_for("playersa", club_id=club.id))
            else:
                flash("This Player Already Exists!")
                return redirect(url_for("add_playera"))

        clubs = list(Club.query.order_by(Club.club_name).all())
        return render_template("add_playera.html", clubs=clubs)


# Route to edit player if admin
@app.route("/edit_playera/<player_id>", methods=["GET", "POST"])
def edit_playera(player_id):
    if session["user"] != "admin":
        return redirect(url_for("playersa", club_id=0))
    else:
        clubs = list(Club.query.order_by(Club.club_name).all())
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
            mongo.db.players.update_one(
                {"_id": ObjectId(player_id)}, {"$set": submit})
            flash("Player Successfully Updated!")
            return redirect(url_for("playersa", club_id=0))
        return render_template("edit_playera.html", player=player, clubs=clubs)


# Route to delete player if admin
@app.route("/delete_playera/<player_id>")
def delete_playera(player_id):
    if session["user"] != "admin":
        return redirect(url_for("playersa", club_id=0))
    else:
        mongo.db.players.delete_one({"_id": ObjectId(player_id)})
        flash("Player Successfully Deleted!")
        return redirect(url_for("playersa", club_id=0))


# Route to form if user != admin
@app.route("/form")
def form():
    if session["user"] == "admin":
        return redirect(url_for("profile", username=session["user"]))
    else:
        return render_template("form.html")


# Route to confirmation page after form submission
@app.route("/confirmation")
def confirmation():
    if session["user"] == "admin":
        return redirect(url_for("profile", username=session["user"]))
    else:
        return render_template("confirmation.html")
