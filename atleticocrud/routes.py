from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from atleticocrud import app, db, mongo
from atleticocrud.models import Country, League, Club, Player, Users


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
    if  session["user"] != "admin":
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
        clubs = list(Club.query.order_by(Club.club_name).filter(Club.league_id==league_id))
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
        club.club_image_url=request.form.get("club_image_url")
        db.session.commit()
        return redirect(url_for("clubs", league_id=club.league_id))
    return render_template("edit_club.html", club=club)


@app.route("/delete_club/<int:club_id>")
def delete_club(club_id):
    club = Club.query.get_or_404(club_id)
    db.session.delete(club)
    db.session.commit()
    return redirect(url_for("clubs", league_id=club.league_id))


@app.route("/players/<int:club_id>")
def players(club_id):
    if club_id == 0:
        players = list(Player.query.order_by(Player.player_name).all())
        return render_template("players.html", players=players)
    else:
        players = list(Player.query.order_by(Player.player_name).filter(Player.club_id==club_id))
        return render_template("players.html", players=players)


@app.route("/add_player", methods=["GET", "POST"])
def add_player():
    if session["user"] != "admin":
        return redirect(url_for("players", club_id=0))
    else:
        clubs = list(Club.query.order_by(Club.club_name).all())
        if request.method == "POST":
            player = Player(
                player_name=request.form.get("player_name"),
                club_id=request.form.get("club_id")
                )
            db.session.add(player)
            db.session.commit()
            return redirect(url_for("players", club_id=player.club_id))
        return render_template("add_player.html", clubs=clubs)


@app.route("/edit_player/<int:player_id>", methods=["GET", "POST"])
def edit_player(player_id):
    player = Player.query.get_or_404(player_id)
    if request.method == "POST":
        player_name = request.form.get("player_name"),
        db.session.commit()
        return redirect(url_for("players", club_id=player.club_id))
    return render_template("edit_player.html", player=player)


@app.route("/delete_player/<int:player_id>")
def delete_player(player_id):
    player = Player.query.get_or_404(player_id)
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for("players", club_id=player.club_id))


@app.route("/stats/<player_id>")
def stats(player_id):
    stats = mongo.db.player_stats.find_one({"player_id": player_id})
    return render_template("stats.html", stats=stats)


@app.route("/add_stats", methods=["GET", "POST"])
def add_stats():
    if request.method == "POST":
        new_stats = request.form.get("player_id")
        if mongo.db.player_stats.count_documents(
                {"player_id": new_stats}, limit=1) == 0:
            player = Player.query.get_or_404(request.form.get("player_id"))
            stats = {
                "player_id": request.form.get("player_id"),
                "player_name": player.player_name,
                "player_dob": request.form.get("player_dob"),
                "player_nationality": request.form.get("player_nationality"),
                "player_position": request.form.get("player_position")
            }
            mongo.db.player_stats.insert_one(stats)
            return redirect(url_for("stats"))
        else:
            flash("This player already has stats")
            return redirect(url_for("add_stats"))

    players = list(Player.query.order_by(Player.player_name).all())
    return render_template("add_stats.html", players=players)
