from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/courses")
def courses():
    return render_template('courses.html')

@app.route("/news")
def news():
    return render_template('news.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')



# -------Forms--------------------

@app.route("/signup")
def signup():
    return render_template('forms/signup.html')

app.run(debug=True)

