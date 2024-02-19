import os
from functools import wraps
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# @login_required decorator
# https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # no "user" in session
        if "user" not in session:
            flash("You must sign in to access this page")
            return redirect(url_for("sign_in"))
        # user is in session
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if "user" not in session:
        # only if there isn't a current session["user"]
        if request.method == "POST":
            # check if username already exists in db
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                flash("Username already exists")
                return redirect(url_for("sign_up"))

            sign_up = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password"))
            }
            mongo.db.users.insert_one(sign_up)

            # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
            return redirect(url_for("welcome", username=session["user"]))

        return render_template("sign_up.html")
    
    # user is already signed in, direct them the home page
    return redirect("home.html")


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if "user" not in session:
        # only if there isn't a current session["user"]
        if request.method == "POST":
            # check if username exists in db
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                # ensure hashed password matches user input
                if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}!".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "welcome", username=session["user"]))
                else:
                    # invalid password match
                    flash("Incorrect Username and/or Password")
                    return redirect(url_for("sign_in"))

            else:
                # username doesn't exist
                flash("Incorrect Username and/or Password")
                return redirect(url_for("sign_in"))
        return render_template("sign_in.html")
    
    # user is already signed in, direct them the home page
    return redirect("home.html")


@app.route("/welcome/<username>", methods=["GET", "POST"])
@login_required
def welcome(username):
    if "user" not in session:
        flash("You must sign in to access this page.")
        return redirect(url_for("sign_in"))

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("welcome.html", username=username)

    return redirect(url_for("sign_in"))


@app.route("/sign_out")
@login_required
def sign_out():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("sign_in"))


@app.route("/get_blog_posts")
def get_blog_posts():
    # find all blog posts
    blog_posts = list(mongo.db.blog_posts.find().sort("date_created", 1))
    return render_template("blog_posts.html", blog_posts=blog_posts)


@app.route("/read_post/<blog_post_id>", methods=["GET", "POST"])
def read_post(blog_post_id):
    # displaying a blog post on a separate page
    mongo.db.blog_posts.find_one({"_id": ObjectId(blog_post_id)})

    blog_post = mongo.db.blog_posts.find_one({"_id": ObjectId(blog_post_id)})
    comments = list(mongo.db.comments.find({"blog_post_id": ObjectId(blog_post_id)}))
    return render_template("read_post.html", blog_post=blog_post, comments=comments)


@app.route("/add_blog_post", methods=["GET", "POST"])
@login_required
def add_blog_post():
    # adding a new blog post
    # admin only page
    if "user" not in session or session["user"].lower() != "admin":
        flash("Access denied. You must be an Admin to add blog posts.")
        return redirect(url_for("get_blog_posts"))

    if request.method == "POST":
        is_new = "on" if request.form.get("is_new") else "off"
        blog_post = {
            "category_name": request.form.get("category_name"),
            "headline": request.form.get("headline"),
            "intro": request.form.get("intro"),
            "post_body": request.form.get("post_body"),
            "image_url": request.form.get("image_url"),
            "date_created": request.form.get("date_created"),
            "is_new": is_new,
            "created_by": session["user"]
        }
        mongo.db.blog_posts.insert_one(blog_post)
        flash("New Blog Post Successfully Added")
        return redirect(url_for("get_blog_posts"))

    # generate the form to insert new blog post
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_blog_post.html", categories=categories)


@app.route("/edit_blog_post/<blog_post_id>", methods=["GET", "POST"])
@login_required
def edit_blog_post(blog_post_id):
    # editing a chosen blog post
    # admin only page
    if "user" not in session or session["user"].lower() != "admin":
        flash("Access denied. You must be an Admin to edit blog posts.")
        return redirect(url_for("get_blog_posts"))

    if request.method == "POST":
        is_new = "on" if request.form.get("is_new") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "headline": request.form.get("headline"),
            "intro": request.form.get("intro"),
            "post_body": request.form.get("post_body"),
            "image_url": request.form.get("image_url"),
            "date_created": request.form.get("date_created"),
            "is_new": is_new,
            "created_by": session["user"]
        }
        mongo.db.blog_posts.replace_one({"_id": ObjectId(blog_post_id)}, submit)
        flash("Blog Post Successfully Updated")

    # generate the form to edit a chosen blog post
    blog_post = mongo.db.blog_posts.find_one({"_id": ObjectId(blog_post_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_blog_post.html", blog_post=blog_post, categories=categories)


@app.route("/delete_blog_post/<blog_post_id>")
@login_required
def delete_blog_post(blog_post_id):
    # deleting a chosen blog post
    # admin only page
    if "user" not in session or session["user"].lower() != "admin":
        flash("Access denied. You must be an Admin to delete blog posts.")
        return redirect(url_for("get_blog_posts"))

    mongo.db.blog_posts.delete_one({"_id": ObjectId(blog_post_id)})
    flash("Blog Post Successfully Deleted")
    return redirect(url_for("get_blog_posts"))


@app.route("/add_comment/<blog_post_id>", methods=["GET", "POST"])
@login_required
def add_comment(blog_post_id):
    # adding a new comment
    # for Registered Users only
    if "user" not in session:
        flash("Access Denied. Only Registered Users can add comments.")
        return redirect(request.referrer)

    if request.method == "POST":
        comment = {
            "comment_content": request.form.get("comment_content"),
            "blog_post_id" : ObjectId(blog_post_id),
            "username": session["user"]
            }
        mongo.db.comments.insert_one(comment)
        flash("New Comment Successfully Added")
        return redirect(url_for("read_post", blog_post_id=blog_post_id))

    return render_template("read_post.html")


@app.route("/edit_comment/<comment_id>", methods=["POST"])
@login_required
def edit_comment(comment_id):
    comment = mongo.db.comments.find_one({"_id": ObjectId(comment_id)})

    # feature available only to the user who created a chosen commit or an admin
    if session["user"].lower() != comment["username"].lower() or session["user"].lower() != "admin":
        flash("Access Denied. You do not own this comment.")
        return redirect(request.referrer)

    # editing a comment
    if request.method == "POST":
        edited_content = request.form.get("edited_comment_content")
        mongo.db.comments.update_one(
            {"_id": ObjectId(comment_id)},
            {"$set": {"comment_content": edited_content}}
        )
        flash("Comment Successfully Edited")
        return redirect(request.referrer)


@app.route("/delete_comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = mongo.db.comments.find_one({"_id": ObjectId(comment_id)})

    # feature available only to the user who created a chosen commit or an admin
    if session["user"].lower() != comment["username"].lower() or session["user"].lower() != "admin":
        flash("Access Denied. You do not own this comment.")
        return redirect(request.referrer)

    # deleting a comment
    mongo.db.comments.delete_one({"_id": ObjectId(comment_id)})
    flash("Comment Successfully Deleted")
    return redirect(request.referrer)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
