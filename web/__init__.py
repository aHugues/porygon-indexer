from flask import Flask
from .views import main_views

def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.register_blueprint(main_views)
    return app