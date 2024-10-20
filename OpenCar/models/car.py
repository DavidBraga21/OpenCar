from models import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)
    is_reserved = db.Column(db.Boolean, default=False)
    stock = db.Column(db.Integer, nullable=False, default=1)
    image_url = db.Column(db.String(255), nullable=False) 
