from flask import Blueprint

main_views = Blueprint('main_views', __name__)

@main_views.route('/')
def hello_world():
    return 'Flask Dockerized'