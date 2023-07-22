from flask import Blueprint, render_template, request, flash
#from email_validator import validate_email

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    #info inputted when accessing this route
    data = request.form
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "Logout"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first-name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        #email_info = validate_email(email, check_deliverability=True)
        #if not email_info:


        
    return render_template("sign_up.html")