"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

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
    posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    return render_template("/homepage.html", users=users, posts=posts)


@app.route("/add-user")
def form():
    """Takes user to add users form"""
    return render_template("/add-user.html")


@app.route("/add-user", methods=["POST"])
def add_user():
    """Add user and redirect to list"""

    first = request.form['first_name']
    last = request.form['last_name']
    image = request.form['image_url']

    new_user = User(first_name=first, last_name=last, image_url=image)
    db.session.add(new_user)
    db.session.commit()

    return render_template("detail.html", user=new_user)


@app.route("/<userId>")
def user(userId):
    user = User.query.get(userId)
    posts = Post.query.filter_by(user_id=userId).all()

    return render_template("detail.html", user=user, posts=posts)


@app.route("/posts")
def posts():
    users = User.query.all()
    posts = Post.query.all()
    return render_template("/posts.html", users=users, posts=posts)


@app.route("/all-users")
def all_users():
    users = User.query.all()
    return render_template("all-users.html", users=users)


@app.route("/new-post", methods=["POST"])
def new_post():
    user = request.form['user']
    return render_template("/new-post.html", user=user)


@app.route("/add-post", methods=["POST"])
def add_post():
    userId = request.form['user-id']
    title = request.form['title']
    content = request.form['content']
    # first_name = request.form['first_name']
    # last_name = request.form['last_name']
    # user = User.query.filter(
    #     User.first_name == first_name, User.last_name == last_name).first()
    # userId = user.id
    new_post = Post(title=title, content=content, user_id=userId)
    db.session.add(new_post)
    db.session.commit()
    return posts()
