from project import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skills = db.Column(db.ARRAY(db.String(50)))
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(2000), unique=False, nullable=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

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
    requiredSkills = db.Column(db.ARRAY(db.String(50)))
    clubName = db.Column(db.String(120), unique=True, nullable=False)
    imageFile = db.Column(db.String(20), nullable=False, default='default.jpg')
    members = db.relationship('User', backref='member', lazy=True)
    description = db.Column(db.String(2000), unique=False, nullable=True)
    def __repr__(self):
        return f"Club('{self.clubName}', '{self.imageFile}')"