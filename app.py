import os
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


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_blog_posts")
def get_blog_posts():
    blog_posts = list(mongo.db.blog_posts.find().sort("date_created", 1))
    return render_template("blog_posts.html", blog_posts=blog_posts)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
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


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
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


@app.route("/welcome/<username>", methods=["GET", "POST"])
def welcome(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("welcome.html", username=username)

    return redirect(url_for("sign_in"))


@app.route("/sign_out")
def sign_out():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("sign_in"))


@app.route("/read_post/<blog_post_id>")
def read_post(blog_post_id):
    mongo.db.blog_posts.find_one({"_id": ObjectId(blog_post_id)})

    blog_post = mongo.db.blog_posts.find_one({"_id": ObjectId(blog_post_id)})
    return render_template("read_post.html", blog_post=blog_post)


@app.route("/add_blog_post", methods=["GET", "POST"])
def add_blog_post():
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

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_blog_post.html", categories=categories)


@app.route("/edit_blog_post/<blog_post_id>", methods=["GET", "POST"])
def edit_blog_post(blog_post_id):
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

    blog_post = mongo.db.blog_posts.find_one({"_id": ObjectId(blog_post_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_blog_post.html", blog_post=blog_post, categories=categories)


@app.route("/delete_blog_post/<blog_post_id>")
def delete_blog_post(blog_post_id):
    mongo.db.blog_posts.delete_one({"_id": ObjectId(blog_post_id)})
    flash("Blog Post Successfully Deleted")
    return redirect(url_for("get_blog_posts"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
