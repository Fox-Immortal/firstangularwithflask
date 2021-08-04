from flask import render_template
from project import app
from project.models import User, Admin_User

#every route should be added here so the server know how to handle these urls 

@app.route("/")
@app.route("/main")
def home():
    return render_template("index.html")

