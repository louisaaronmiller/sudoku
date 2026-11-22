from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()


def create_app():
    app = Flask(__name__)

    print(app.root_path)
    print(app.template_folder)
    print(app.jinja_loader.searchpath)

    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

    from .views import views

    app.register_blueprint(views)

    return app

