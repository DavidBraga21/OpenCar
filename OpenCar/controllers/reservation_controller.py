from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models.reservation import Reservation
from models.user_dao import UserDAO
from models.car_dao import CarDAO
from models.reservation_dao import ReservationDAO
from datetime import datetime, timedelta

reservation_bp = Blueprint('reservation_bp', __name__)

@reservation_bp.route('/', methods=['GET'])
def get_reservas():
    reservations = ReservationDAO.get_all_reservations()
    return render_template('exibir_reservas.html', reservations=reservations)

@reservation_bp.route('/fazer', methods=['GET', 'POST'])
def fazer_reserva():
    if 'user_id' not in session:
        session['next'] = url_for('reservation_bp.fazer_reserva')
        return redirect(url_for('user_bp.login_usuarios'))
    
    user_id = session['user_id']
    logged_in_user = UserDAO.get_user_by_id(user_id)

    if request.method == 'POST':
        user_name = request.form['user_name']
        car_id = int(request.form['car_id'])
        days = int(request.form['days'])
        reservation_date_str = request.form['reservation_date']

        if user_name != logged_in_user.name:
            flash("O nome do usuário não corresponde ao usuário logado.", "danger_fazer_reserva")
            return redirect(url_for('reservation_bp.fazer_reserva'))

        try:
            reservation_date = datetime.strptime(reservation_date_str, '%Y-%m-%d').date()
            if reservation_date < datetime.today().date():
                flash("A data de início da reserva não pode ser uma data passada.", "danger_fazer_reserva")
                return redirect(url_for('reservation_bp.fazer_reserva'))
        except ValueError:
            flash("Formato de data inválido.", "danger_fazer_reserva")
            return redirect(url_for('reservation_bp.fazer_reserva'))

        if days <= 0:
            flash("O número de dias deve ser maior que 0.", "danger_fazer_reserva")
            return redirect(url_for('reservation_bp.fazer_reserva'))

        car = CarDAO.get_car_by_id(car_id)
        if not car or car.stock <= 0:
            flash("Carro não disponível.", "danger_fazer_reserva")
            return redirect(url_for('reservation_bp.fazer_reserva'))

        car.stock -= 1
        CarDAO.update_car(car)

        total_value = days * car.price_per_day
        reservation = Reservation(user_id=user_id, car_id=car.id, days=days, total_value=total_value)
        reservation.reservation_date = reservation_date
        reservation.end_date = reservation_date + timedelta(days=days)

        ReservationDAO.add_reservation(reservation)

        return redirect(url_for('index'))

    cars = CarDAO.get_all_cars()
    return render_template('fazer_reserva.html', cars=cars, logged_in_user=logged_in_user)

@reservation_bp.route('/perfil', methods=['GET'])
def perfil_usuario():
    if 'user_id' not in session:
        return redirect(url_for('user_bp.login_usuarios'))

    user_id = session['user_id']
    user = UserDAO.get_user_by_id(user_id)
    reservations = ReservationDAO.get_reservations_by_user_id(user_id)

    return render_template('perfil_usuario.html', user=user, reservations=reservations)
