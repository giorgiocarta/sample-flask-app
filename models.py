from app import db


class Movie(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self) -> str:
        return "<Title: {}>".format(self.title)
