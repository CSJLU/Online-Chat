from flask import Blueprint

#blueprints contains all the routes
views = Blueprint('views', __name__)

@views.route('/')
def home():
    pass