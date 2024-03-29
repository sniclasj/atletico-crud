from atleticocrud import db


class Country(db.Model):
    # schema for the Country model
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(25), unique=True, nullable=False)
    country_image_url = db.Column(db.String(250), unique=True, nullable=True)
    leagues = db.relationship(
        "League", backref="country", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return
        f"#{self.country_name} - Country Image URL: {self.country_image_url}"


class League(db.Model):
    # schema for the League model
    id = db.Column(db.Integer, primary_key=True)
    league_name = db.Column(db.String(50), unique=True, nullable=False)
    league_image_url = db.Column(db.String(250), unique=True, nullable=True)
    country_id = db.Column(db.Integer, db.ForeignKey(
        "country.id", ondelete="CASCADE"), nullable=False)
    clubs = db.relationship(
        "Club", backref="league", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return(
            f"#{self.country_id} - "
            f"# League: {self.league_name} - "
            f"# League Image URL: {self.league_image_url}"
        )


class Club(db.Model):
    # schema for the Club model
    id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String(50), unique=True, nullable=False)
    club_image_url = db.Column(db.String(250), unique=True, nullable=True)
    league_id = db.Column(db.Integer, db.ForeignKey(
        "league.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return(
            f"#{self.league_id} - "
            f"# Club: {self.club_name} - "
            f"# Club Image URL: {self.club_image_url}"
            )


class Users(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.user_name}"
