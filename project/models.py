from datascience.tables import Table
from project import db, api, app
import requests
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class User_Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    club_guy = db.Column(db.Integer, db.ForeignKey('user.id'))
    club_skills = db.Column(db.Integer, db.ForeignKey('club.id'))

class Skill(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    skilled_guy_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    club_skills = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    name = db.Column(db.String(30), nullable = False)
    percentage = db.Column(db.Integer)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15))
    name = db.Column(db.String(30), unique=True, nullable=False)
    skills = db.relationship('Skill', backref='skilled_guy', lazy=True)
    clubs = db.relationship('User_Club', backref='clubsOfMember', lazy=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(2000), unique=False, nullable=True)
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.image_file}')"

class Admin_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(2000), unique=False, nullable=True)
    def __repr__(self):
        return f"Admin_User('{self.username}', '{self.email}', '{self.image_file}')"

class Club(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    requiredSkills = db.relationship('Skill', backref='requiredSkillForTheClub', lazy=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    imageFile = db.Column(db.String(20), nullable=False, default='default.jpg')
    members = db.relationship('User_Club', backref='memberOfClub', lazy=True)
    description = db.Column(db.String(2000), unique=False, nullable=True)
    def __repr__(self):
        return f"Club('{self.clubName}', '{self.imageFile}')"
    