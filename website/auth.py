from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

#ADD A ROUTE THAT APPEARS AFTER LOGIN FOR CHAT ROOM

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
        last_name = request.form.get('last-name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than four characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than one character', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than one character', category='error')
        elif password1 != password2:
            flash('Passwords are not the same', category='error')
        elif len(password1) < 7:
            flash('Password must be at least seven characters', category='error') 
        else: 
            flash('Registration successful', category='success')
        


        
    return render_template("sign_up.html")