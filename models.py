"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User."""

    __tablename__ = "users"

    def __repr__(self):
        u = self
        return f"<User {u.id}: {u.first_name} {u.last_name}>"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.Text, nullable=False, default='John')
    last_name = db.Column(db.Text, nullable=False, default='Smith')
    image_url = db.Column(
        db.Text, default="https://img.freepik.com/free-photo/handsome-confident-smiling-man-with-hands-crossed-chest_176420-18743.jpg?w=2000")
    posts = db.relationship('Post', backref="user",
                            cascade="all, delete-orphan")


class Post(db.Model):
    """Post."""

    __tablename__ = "posts"

    def __repr__(self):
        p = self
        return f"<Post {p.id}: title = {p.title}; content = {p.content}; user_id = {p.user_id}>"

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
    # tags = db.relationship(
    #     'Tag', secondary='tagged_posts', cascade="all,delete", backref="posts")


class Tag(db.Model):
    """Tag"""

    __tablename__ = "tags"

    def __repr__(self):
        t = self
        return f"<tag {t.id}: {t.name}>"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.Text, nullable=False)
    posts = db.relationship(
        'Post', secondary='tagged_posts', cascade="all,delete", backref="tags",)


class Tag_Post(db.Model):
    """Tagged Posts"""

    __tablename__ = "tagged_posts"

    def __repr__(self):
        tp = self
        return f"<post_id = {tp.post_id} tag_id = {tp.tag_id}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey(
        'tags.id'), nullable=False)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
