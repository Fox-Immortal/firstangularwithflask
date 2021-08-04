from flask import render_template, flash, redirect, url_for
from project import app, bcrypt
# from flask_login import login_user, current_user, logout_user, login_required
from project.models import User, Admin_User
from project.forms import LoginForm 

# I'll make 2 routes for the login page or it might be the first one
# why

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # if user and bcrypt.check_password_hash(user.password, form.password.data):
        if form.email.data == 'admin@demo.cc':
            return redirect(url_for('main'))
        else :
            flash('Login Unsuccessful. Please check E-mail and password', 'danger')
    return render_template("index.html", title='Login', form=form)

@app.route("/main", methods=['GET', 'POST'])
def main():
    form = LoginForm()
    return render_template("index.html", title='Login', form=form)