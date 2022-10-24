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

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    url = request.form['url']

    user = User(first_name=first_name, last_name=last_name, url=url)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/{user.id}")

@app.route("/int:user_id")
def show_user(user_id):
    """show info on single user"""

    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)