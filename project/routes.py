from flask import render_template, flash, redirect, url_for
from project import app, bcrypt
# from flask_login import login_user, current_user, logout_user, login_required
# from project.models import User, Admin_User
# from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
# from project.forms import LoginForm, RegistrationForm


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")



# @app.route("/api/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         # if user and bcrypt.check_password_hash(user.password, form.password.data):
#         if form.email.data == 'admin@demo.cc':
#             return "YOU HAVE LOGGED IN"
#         else :
#             flash('Login Unsuccessful. Please check E-mail and password', 'danger')
#     return render_template(url_for('ez'))

# @app.route("/api/register", methods=['GET', 'POST'])
# def main():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         user = User(username=form.username.data, email = form.email.data, password = hashed_password)
#         db.session.add(user)
#         db.session.commit()
#         flash(f' Your account has been created {form.username.data}! You now can log in.', 'success')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)