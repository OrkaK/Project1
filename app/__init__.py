from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)

    from app.routes.users import users_bp
    from app.routes.home import home_bp

    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(home_bp)

    return app
