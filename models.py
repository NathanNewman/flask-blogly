"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.Text, nullable=False, default='John')
    last_name = db.Column(db.Text, nullable=False, default='Smith')
    image_url = db.Column(db.Text, default="https://img.freepik.com/free-photo/handsome-confident-smiling-man-with-hands-crossed-chest_176420-18743.jpg?w=2000")
    posts = db.relationship('Post')

class Post(db.Model):
    """Post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        nullable=False)
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('users.id'), 
        nullable=False)

    user = db.relationship('User')


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)