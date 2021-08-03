from flask import render_template, flash, redirect
from project import app, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from project.models import User, Admin_User
from project.forms import LoginForm

# I'll make 2 routes for the login page or it might be the first one
# why

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    print("TEST")
    form = LoginForm()
    user = User.query.filter_by(email=form.email.data).first()
    # if user and bcrypt.check_password_hash(user.password, form.password.data):
    if form.email == 'admin@demo.cc':
        return redirect(url_for('main'))
    else :
        flash('Login Unsuccessful. Please check E-mail and password', 'danger')
    return render_template("index.html", title='Login', form=form)

@app.route("/main")
def main():
    return render_template("index.html", title='Home', form=form)