from flask import render_template, flash, redirect, url_for, request, jsonify, session
from project import app, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from project.models import *
from project import db,app , bcrypt, mail
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from project.forms import *
from flask_mail import Message



BASE = "127.0.0.1/5000"

@app.route("/main")
@app.route("/club")
@app.route("/clubs")
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/api/login", methods=['POST'])
def login():
    json_data = request.json
    user = User.query.filter_by(email=json_data['email']).first()
    if user and bcrypt.check_password_hash(user.password, json_data['password']):
        session['logged_in'] = True
        status = True
    else :
        status = False
    return jsonify({'result': status})

@app.route('/api/register', methods=['GET', 'POST'])
def register():
    json_data = request.json
    user = User(
        name=json_data['name'],
        email=json_data['email'],
        password=json_data['password']
    )
    search_for_similar = User.query.filter_by(email=user.email).first()
    if not search_for_similar:
        user.password = bcrypt.generate_password_hash(user.password).decode('utf-8')
        db.session.add(user)
        db.session.commit()
        db.session.close()
        status = 'success'
    else :
        status = 'this user is already registered'

    return jsonify({'result': status})

@app.route('/api/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'result': 'success'})

@app.route('/api/status')
def status():
    if session.get('logged_in'):
        if session['logged_in']:
            return jsonify({'result': True})
        else:
            return jsonify({'result' : False})
    else:
        return jsonify({'result': False})

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='Student-Link@outlook.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
    {url_for('reset_token', token = token, _external = True)}
    If you did not make this request then simply ignore this email and no change has been made
    '''
    mail.send(msg)

@app.route("/api/reset_password", methods=['GET', 'POST'])
def reset_request():
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route("/api/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)