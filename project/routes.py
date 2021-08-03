from flask import render_template
from project import app
from project.models import User, Admin_User
from project.forms import LoginForm

# I'll make 2 routes for the login page or it might be the first one
# why

@app.route("/")
@app.route("/login")
def home():
    form = LoginForm
    return render_template("index.html", title='Login', form=form)

