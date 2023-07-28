from flask import Flask
from .admin import admin_bp
from .auth import auth_bp
from .clinic import clinic_bp
from .meal import meal_bp
from .notification import notification_bp
from .predict import predict_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(clinic_bp)
    app.register_blueprint(meal_bp)
    app.register_blueprint(notification_bp)
    app.register_blueprint(predict_bp)

    return app