from datascience.tables import Table
from project import db
import requests
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

BASE = "http://127.0.0.1:5000/"

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("name", type=str, help="Name of the video is required")
user_update_args.add_argument("views", type=int, help="Views of the video")
user_update_args.add_argument("likes", type=int, help="Liked of the video")


class User_Club(db.Model, Resource):
    id = db.Column(db.Integer, primary_key=True)
    club_guy = db.Column(db.Integer, db.ForeignKey('user.id'))
    club_skills = db.Column(db.Integer, db.ForeignKey('club.id'))

class Skill(db.Model, Resource) :
    id = db.Column(db.Integer, primary_key=True)
    skilled_guy_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    club_skills = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    name = db.Column(db.String(30), nullable = False)
    percentage = db.Column(db.Integer)

class User(db.Model, Resource):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    skills = db.relationship('Skill', backref='skilled_guy', lazy=True)
    clubs = db.relationship('User_Club', backref='clubsOfMember', lazy=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(2000), unique=False, nullable=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    @marshal_with(user_resource_fields)
    def post(self, user_id):
        result = User.query.filter_by(user_id).first()
        if not result:
            abort(404, message="Could not find a user with that id...")
        response = requests.patch(BASE + "User/" + user_id, user_resource_fields)
        print(response.json())
        return result

class Admin_User(db.Model, Resource):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(2000), unique=False, nullable=True)
    def __repr__(self):
        return f"Admin_User('{self.username}', '{self.email}', '{self.image_file}')"

class Club(db.Model, Resource) :
    id = db.Column(db.Integer, primary_key=True)
    requiredSkills = db.relationship('Skill', backref='requiredSkillForTheClub', lazy=True)
    clubName = db.Column(db.String(120), unique=True, nullable=False)
    imageFile = db.Column(db.String(20), nullable=False, default='default.jpg')
    members = db.relationship('User_Club', backref='memberOfClub', lazy=True)
    description = db.Column(db.String(2000), unique=False, nullable=True)
    def __repr__(self):
        return f"Club('{self.clubName}', '{self.imageFile}')"
    
