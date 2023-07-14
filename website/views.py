from flask import Blueprint, render_template

#blueprints contains all the routes
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")