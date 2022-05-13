from atleticocrud import db


class Country(db.Model):
    # schema for the Country model
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(25), unique=True, nullable=False)
    leagues = db.relationship("League", backref="country", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.country_name


class League(db.Model):
    # schema for the League model
    id = db.Column(db.Integer, primary_key=True)
    league_name = db.Column(db.String(50), unique=True, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("country.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.country_id} - League: {self.league_name}"


class Club(db.Model):
    # schema for the Club model
    id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String(50), unique=True, nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey("league.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Club: {1}".format(
            self.league_id, self.club_name
        )


class Player(db.Model):
    # schema for the Player model
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(50), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey("club.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Player Name: {1}".format(
            self.club_id, self.player_name
        )