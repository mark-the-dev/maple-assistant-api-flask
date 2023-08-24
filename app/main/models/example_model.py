from .. import db

class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)