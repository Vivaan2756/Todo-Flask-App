from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db=SQLAlchemy()
login_manager = LoginManager()
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    return app
   