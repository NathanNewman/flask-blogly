"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "SECRET!"

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def root():
    """List users and show add form"""
    
    return redirect("/homepage")

@app.route("/homepage")
def homepage():
    """List users"""
    users = User.query.all()
    return render_template("/homepage.html", users=users)

@app.route("/form")
def form():
    """Takes user to add users form"""
    return render_template("/form.html")

@app.route("/form", methods=["POST"])
def add_user():
    """Add user and redirect to list"""

    first = request.form['first_name']
    last = request.form['last_name']
    image = request.form['image_url']

    new_user = User(first_name=first, last_name=last, image_url=image)
    db.session.add(new_user)
    db.session.commit()
    user = User.query

    return redirect("detail.html", user=user)