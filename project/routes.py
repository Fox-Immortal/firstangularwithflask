import os
import secrets
from PIL import Image
from project.forms import *
from project.models import *
from flask_mail import Message
from project import db, app, bcrypt, mail
from flask_login import login_user, current_user, logout_user, login_required
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask import render_template, flash, redirect, url_for, request, jsonify, session



BASE = "127.0.0.1/5000"

@app.route("/main")
@app.route("/", methods=['GET', 'POST'])
@login_required
def home():
    return render_template("index.html")


@app.route("/api/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    json_data = request.json
    user = User.query.filter_by(email=json_data['email']).first()
    if user and bcrypt.check_password_hash(user.password, json_data['password']):
        session['logged_in'] = True
        status = True
        login_user(user)
    else :
        flash('Login Unsuccessful. Please check E-mail and password', 'danger')
        status = False
    return jsonify({'result': status})

@app.route('/api/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    json_data = request.json
    user = User(
        name=json_data['name'],
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
    logout_user()
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

@app.route("/api/save_picture/", methods=['GET', 'POST'])
@login_required
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/assets/profile_pics', picture_fn)
    output_size = (125, 125)
    newImage = Image.open(form_picture)
    newImage.thumbnail(output_size)
    newImage.save(picture_path)
    return newImage

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