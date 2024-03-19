from flask import Flask
from flask_cors import  CORS


def create_app():
    app = Flask(__name__)   
    CORS(app)
    app.config['UPLOAD_FOLDER']= 'uploads'


    with app.app_context():
        from . import views

    return app