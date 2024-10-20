from werkzeug.security import generate_password_hash, check_password_hash
from . import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False) 
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)
    reservations = db.relationship('Reservation', backref='user', lazy=True)
    senha_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.senha_hash, senha)
