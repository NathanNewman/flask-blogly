"""Seed file to make sample data for users db."""

from models import User, db
from app import app

#Create all tables
db.drop_all
db.create_all

# If table isn't empty, emty it
User.query.delete()

# Add users
alan = User(first_name='Alan', last_name='Alda', url='https://images.pexels.com/photos/2379004/pexels-photo-2379004.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')
joel = User(first_name='Joel', last_name='Burton', url='https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bWFufGVufDB8fDB8fA%3D%3D&w=1000&q=80')
jane = User(first_name='Jane', last_name='Smith', url='https://media.istockphoto.com/photos/beautiful-successful-latin-woman-smiling-picture-id1369508766?b=1&k=20&m=1369508766&s=170667a&w=0&h=xr3pk8VTmDoC9JXzEqMPL_4jZLiyIJWUMzKrBlVQiPI=')

# Add new objects to session
db.session.add(alan)
db.session.add(joel)
db.session.add(jane)

# Commit
db.session.commit()