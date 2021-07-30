from flask import render_template
from firststuff import app

@app.route("/")
def home():
    return "Hello World!"