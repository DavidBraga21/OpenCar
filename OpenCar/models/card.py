from . import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(50), nullable=False)
    card_number = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    security_code = db.Column(db.String(4), nullable=False)
    user = db.relationship('User', backref='card', uselist=False)
