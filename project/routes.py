from flask import render_template, flash, redirect, url_for, request, jsonify, session
from project import app, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from project.models import *
from project import db
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from project.forms import LoginForm, RegistrationForm


BASE = "127.0.0.1/5000"

@app.route("/", methods=['GET', 'POST'])
def test():
    return render_template("test.html")



@app.route("/api/login", methods=['POST'])
def login():
    json_data = request.json
    user = User.query.filter_by(email=json_data['email']).first()
    if user and bcrypt.check_password_hash(user.password, json_data['password']):
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
        username=json_data['username'],
        email=json_data['email'],
        password=json_data['password']
    )
    search_for_similar = User.query.filter_by(email=user.email).first()
    if not search_for_similar:
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

