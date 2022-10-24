"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.Text, nullable=False, default='John')
    last_name = db.Column(db.Text, nullable=False, default='Smith')
    image_url = db.Column(db.Text)

    def greet(self):
        """Greet using name"""
        return f"Hi! I'm {self.first_name}. Nice to meet you."

    def __repr__(self):
        """Show info about user"""

        u = self
        return f"<User {u.id} {u.first_name} {u.last_name} {u.url}"
