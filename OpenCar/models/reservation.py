from datetime import date, timedelta
from . import db

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    days = db.Column(db.Integer, nullable=False)
    total_value = db.Column(db.Float, nullable=False)
    reservation_date = db.Column(db.Date, nullable=True, default=date.today)
    end_date = db.Column(db.Date, nullable=True)

    def __init__(self, user_id, car_id, days, total_value, reservatio_date=0, end_date=0):
        self.user_id = user_id
        self.car_id = car_id
        self.days = days
        self.total_value = total_value
        self.reservation_date = date.today()
        self.end_date = self.reservation_date + timedelta(days=days)

  