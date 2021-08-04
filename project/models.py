from datascience.tables import Table
from project import db
from sqlalchemy import *
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

user_resource_fields = {
    'id': fields.Integer,
    'name' : fields.String,
    'password' : fields.Integer,
    'email' : fields.String,
    'phone_number' : fields.Integer
}

club_resource_fields = {
    'id': fields.Integer,
    'clubName' : fields.String,
    'description' : fields.String,
    'owner_id' : fields.Integer
}


skill_resource_fields = {
    'id': fields.Integer,
    'name' : fields.String,
    'percentage' : fields.Integer
}

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("username", type=str, help="Username of the User is required", required=True)
user_put_args.add_argument("id", type=int, help="ID of the user", required=True)
user_put_args.add_argument("skills", type=int, help="Liked of the video", required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("name", type=str, help="Name of the video is required")
user_update_args.add_argument("views", type=int, help="Views of the video")
user_update_args.add_argument("likes", type=int, help="Liked of the video")

User_Club = Table('User_Club', MetaData(), db.Column('id', db.Integer, primary_key=True), db.Column('user_id', db.Integer, db.ForeignKey('User.id')), db.Column('club_id', db.Integer, db.ForeignKey('Club.id')))

class Skill(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    skilled_guy_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    club_skills = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    name = db.Column(db.String(30), nullable = False)
    percentage = db.Column(db.Integer)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    skills = db.relationship('Skill', backref='skilled_guy', lazy=True)
    clubs = db.relationship('User_Club', secondary=User_Club, backref='clubsOfMember')
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(2000), unique=False, nullable=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    @marshal_with(user_resource_fields)
    def get(self, user_id):
        result = User.query.filter_by(user_id).first()
        if not result:
            abort(404, message="Could not find a user with that id...")
        return result

class Admin_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(2000), unique=False, nullable=True)
    def __repr__(self):
        return f"Admin_User('{self.username}', '{self.email}', '{self.image_file}')"

class Club(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    requiredSkills = db.relationship('Skill', backref='requiredSkillForTheClub', lazy=True)
    clubName = db.Column(db.String(120), unique=True, nullable=False)
    imageFile = db.Column(db.String(20), nullable=False, default='default.jpg')
    members = db.relationship('User_Club', secondary=User_Club, backref='memberOfClub')
    description = db.Column(db.String(2000), unique=False, nullable=True)
    def __repr__(self):
        return f"Club('{self.clubName}', '{self.imageFile}')"


