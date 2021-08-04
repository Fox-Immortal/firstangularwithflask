from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
app.config['SECRET_KEY'] = '2d4904a0818e55ebf6d4c38e8af9b56c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)
bcrypt = Bcrypt(app)

from project.models import *

user_resource_fields = {
    'id': fields.Integer,
    'name' : fields.String,
    'password' : fields.String,
    'email' : fields.String
}

club_resource_fields = {
    'id': fields.Integer,
    'clubName' : fields.String,
    'description' : fields.String
}


skill_resource_fields = {
    'id': fields.Integer,
    'name' : fields.String,
    'percentage' : fields.Integer
}


class User_Api(Resource):
    @marshal_with(user_resource_fields)
    def get(self, user_id):
        result = User.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="Could not find a User with that id...")
        return result

class Club_Api(Resource):
    @marshal_with(club_resource_fields)
    def get(self, club_id):
        result = Club.query.filter_by(id=club_id).first()
        if not result:
            abort(404, message="Could not find a Club with that id...")
        return result


api.add_resource(User_Api, "/user/<int:user_id>")
api.add_resource(Club_Api, "/club/<int:club_id>")


from project import routes