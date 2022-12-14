"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, Tag_Post

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
    tagged_posts = Tag_Post.query.all()
    tags = Tag.query.all()
    return render_template("detail.html", user=user, posts=posts, tagged_posts=tagged_posts, tags=tags)


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
    new_post = Post(title=title, content=content, user_id=userId)
    db.session.add(new_post)
    db.session.commit()
    return render_template("post-detail.html", post=new_post)


@app.route("/edit-post_html", methods=["POST"])
def edit_post_html():
    postId = request.form['post-id']
    return render_template("/edit-post.html", post=postId)


@app.route("/edit-post", methods=["POST"])
def edit_post():
    postId = request.form['post-id']
    postId = int(postId)
    title = request.form['title']
    content = request.form['content']
    post = Post.query.filter_by(id=postId).first()
    post.title = title
    post.content = content
    userId = post.user_id
    db.session.commit()
    return redirect(f"/{userId}")


@app.route("/delete-post", methods=["POST"])
def delete_post():
    postId = request.form['post-id']
    postId = int(postId)
    post = Post.query.filter_by(id=postId).first()
    userId = post.user_id
    Tag_Post.query.filter_by(post_id=postId).delete()
    Post.query.filter_by(id=postId).delete()
    db.session.commit()
    return redirect(f"/{userId}")


@app.route("/edit-user", methods=["POST"])
def edit_user_html():
    userId = request.form['user-id']
    int(userId)
    user = User.query.get(userId)
    return render_template('/edit-user.html', user=user)


@app.route("/editted-user", methods=["POST"])
def edit_user():
    userId = request.form['id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    current_user = User.query.get(userId)
    current_user.first_name = first_name
    current_user.last_name = last_name
    current_user.image_url = image_url
    db.session.commit()
    return redirect(f"/{userId}")


@app.route("/delete-user", methods=["POST"])
def delete_user():
    userId = request.form['user']
    int(userId)
    Post.query.filter_by(user_id=userId).delete()
    User.query.filter_by(id=userId).delete()
    db.session.commit()
    return redirect('/all-users')


@app.route("/tag")
def tag_html():
    posts = Post.query.all()
    return render_template("/new-tag.html", posts=posts)


@app.route("/new-tag", methods=["POST"])
def new_tag():
    tagName = request.form['tag-name']
    postIds = request.form.getlist('post-id')
    new_tag = Tag(name=tagName)
    db.session.add(new_tag)
    db.session.commit()
    tag = Tag.query.filter_by(name=tagName).first()
    tagId = tag.id
    for post in postIds:
        new_tp = Tag_Post(post_id=post, tag_id=tagId)
        db.session.add(new_tp)
    db.session.commit()
    return redirect("/tags")


@app.route("/edit-tag/<tagId>")
def edit_tag_html(tagId):
    tag = Tag.query.get(tagId)
    posts = Post.query.all()
    return render_template("/edit-tag.html", tag=tag, posts=posts)


@app.route("/tags")
def tags():
    tags = Tag.query.all()
    return render_template("/tags.html", tags=tags)


@app.route('/editted-tag', methods=["POST"])
def editted_tag():
    tagId = request.form['tag-id']
    tagName = request.form['tag-name']
    postIds = request.form.getlist('post-id')
    tag = Tag.query.get(tagId)
    tag.name = tagName
    Tag_Post.query.filter_by(tag_id=tagId).delete()
    for post in postIds:
        new_tp = Tag_Post(post_id=post, tag_id=tagId)
        db.session.add(new_tp)
    db.session.commit()
    return redirect("/tags")


@app.route('/delete-tag', methods=["POST"])
def delete_tag():
    tagId = request.form['tag-id']
    Tag_Post.query.filter_by(tag_id=tagId).delete()
    Tag.query.filter_by(id=tagId).delete()
    db.session.commit()
    return redirect("/tags")
