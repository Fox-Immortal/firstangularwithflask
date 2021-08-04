from flask import render_template, flash, redirect, url_for, request, jsonify, session
from project import app, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from project.models import User, Admin_User
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from project.forms import LoginForm, RegistrationForm


@app.route("/", methods=['GET', 'POST'])
def ez():
    return render_template("test.html")



@app.route("/api/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        json_data = request.json
        user = User.query.filter_by(email=json_data['email']).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
        # if form.email.data == 'admin@demo.cc':
            session['logged_in'] = True
            status = True
        else :
            flash('Login Unsuccessful. Please check E-mail and password', 'danger')
            status = False
    return jsonify({'result': status})

@app.route('/api/register', methods=['GET', 'POST'])
def register():
    json_data = request.json
    user = User(
        email=json_data['email'],
        password=json_data['password']
    )
    try:
        db.session.add(user)
        db.session.commit()
        status = 'success'
    except:
        status = 'this user is already registered'
    db.session.close()
    return jsonify({'result': status})

@app.route('/api/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'result': 'success'})

@app.route("/api/register", methods=['GET', 'POST'])
def main():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f' Your account has been created {form.username.data}! You now can log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)