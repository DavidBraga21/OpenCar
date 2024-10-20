from flask import Blueprint, render_template
from models.car import Car

display_car_bp = Blueprint('display_car', __name__)

@display_car_bp.route('/')
def display_cars():
    cars = Car.query.filter_by(is_reserved=False).all()
    return render_template('display_cars.html', cars=cars)



