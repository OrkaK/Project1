from flask import Flask
from app.models import db
from app.routes.users import users_bp
from app.routes.home import home_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(users_bp)
    app.register_blueprint(home_bp)

    return app
