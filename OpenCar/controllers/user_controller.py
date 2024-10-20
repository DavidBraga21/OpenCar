from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, session
from models.user import User
from models.card import Card
from models.user_dao import UserDAO
from models import db

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone_number = request.form['phone_number']
        email = request.form['email']
        card_name = request.form['card_name']
        card_number = request.form['card_number']
        password = request.form['password']
        security_code = request.form['security_code']
        senha = request.form['senha']

        existing_user = UserDAO.get_user_by_email(email)
        if existing_user:
            flash('E-mail já cadastrado. Por favor, use um e-mail diferente.', 'danger_cadastro')
            return redirect(url_for('user_bp.cadastrar_usuario'))

        card = Card(card_name=card_name, card_number=card_number, password=password, security_code=security_code)
        db.session.add(card)
        db.session.commit()

        user = User(name=name, address=address, phone_number=phone_number, email=email, card_id=card.id)
        user.set_password(senha)

        UserDAO.add_user(user)

        return redirect(url_for('user_bp.login_usuarios'))
    return render_template('cadastrar_usuario.html')

@user_bp.route('/', methods=['GET'])
def get_usuarios():
    users = UserDAO.get_all_users()
    return render_template('exibir_usuarios.html', users=users)

@user_bp.route('/login', methods=['GET', 'POST'])
def login_usuarios():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = UserDAO.get_user_by_email(email)
        if user and user.check_password(senha):
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            flash('E-mail ou senha incorretos.', 'danger_login')
    return render_template('login.html')

@user_bp.route('/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))
