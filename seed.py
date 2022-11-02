"""Seed file to make sample data for users db."""
from app import app
from models import User, Post, Tag, Tag_Post, db

# Create all tables
db.drop_all()
db.create_all()

# If tables aren't empty, emty them
User.query.delete()
Post.query.delete()

# Add users
alan = User(first_name='Alan', last_name='Alda',
            image_url='https://images.pexels.com/photos/2379004/pexels-photo-2379004.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')
joel = User(first_name='Joel', last_name='Burton',
            image_url='https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bWFufGVufDB8fDB8fA%3D%3D&w=1000&q=80')
jane = User(first_name='Jane', last_name='Smith',
            image_url='https://media.istockphoto.com/photos/beautiful-successful-latin-woman-smiling-picture-id1369508766?b=1&k=20&m=1369508766&s=170667a&w=0&h=xr3pk8VTmDoC9JXzEqMPL_4jZLiyIJWUMzKrBlVQiPI=')

# Add posts
# id, title, content, created_at, user_name
hello = Post(
    title='Welcome',
    content='Hi! My name is Alan and I just want to welcome everyone to this website.',
    user_id=1)
first = Post(
    title="First",
    content='Haha! First one to make a post!',
    user_id=2)
wrong = Post(
    title='Joel is wrong!',
    content='Alan was the first to post, not you Joel!',
    user_id=3)
sorry = Post(
    title='Sorry',
    content='Sorry Alan, I guess you beat me. No one had posted at the time I started typing. You must have post while I was writing',
    user_id=2)
np = Post(
    title='NP',
    content='No problem. It actually gave me a laugh.',
    user_id=1)
ego = Post(
    title='Too Much Ego',
    content='This would not be a problem if you did not always try to brag about something.',
    user_id=3)
back_off = Post(
    title='Back Off Jane!',
    content='I said I was sorry Jane. Can you just stop with the nagging already?',
    user_id=2
)

# Add Tags
fun = Tag(name='Fun')
even_more = Tag(name='Even More')
bloop = Tag(name='Bloop')
zope = Tag(name='Zope')

# Add new objects to session
db.session.add(alan)
db.session.add(joel)
db.session.add(jane)
db.session.add(hello)
db.session.add(first)
db.session.add(wrong)
db.session.add(sorry)
db.session.add(np)
db.session.add(ego)
db.session.add(back_off)
db.session.add(fun)
db.session.add(even_more)
db.session.add(bloop)
db.session.add(zope)

# Commit
db.session.commit()
