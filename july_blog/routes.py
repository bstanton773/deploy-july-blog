from  july_blog import app
from flask import render_template

# Home route
@app.route('/')
def home():
    return render_template("home.html")