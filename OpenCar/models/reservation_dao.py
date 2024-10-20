from datetime import date
from . import db
from .reservation import Reservation

class ReservationDAO:
    @staticmethod
    def add_reservation(reservation):
        db.session.add(reservation)
        db.session.commit()
    
    @staticmethod
    def get_all_reservations():
        return Reservation.query.all()
    
    @staticmethod
    def get_reservation_by_id(reservation_id):
        return Reservation.query.get(reservation_id)
    
    @staticmethod
    def get_reservations_by_user_id(user_id):
        return Reservation.query.filter_by(user_id=user_id).all()
    
    @staticmethod
    def get_reservations_by_date(reservation_date):
        return Reservation.query.filter_by(reservation_date=reservation_date).all()
