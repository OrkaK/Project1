from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
def user_list():
    users = User.query.all()
    return render_template('users.html', users=users)

@users_bp.route('/add', methods=['POST'])
def add_user():
    try:
        name = request.form.get('name')
        email = request.form.get('email')

        if name and email:
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

        return redirect(url_for('users.user_list'))
    except Exception as e:
        return f"Error: {e}"

@users_bp.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users.user_list'))
