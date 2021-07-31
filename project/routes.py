from flask import render_template
from project import app
from project.models import User, Admin_User

# I'll make 2 routes for the login page or it might be the first one

@app.route("/")
@app.route("/login")
def home():
    return render_template("index.html")

