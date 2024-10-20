from . import db
from .user import User

class UserDAO:
    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()
    
    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def get_user_by_name(name):
        return User.query.filter_by(name=name).first()

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)