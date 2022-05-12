from atleticocrud import db


class Country(db.Model):
    # schema for the Country model
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(25), unique=True, nullable=False)
    leagues = db.relationship("Leagues", backref="country", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.country_name


class Leagues(db.Model):
    # schema for the League model
    id = db.Column(db.Integer, primary_key=True)
    league_name = db.Column(db.String(50), unique=True, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey("country.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - League: {1}".format(
            self.id, self.league_name
        )