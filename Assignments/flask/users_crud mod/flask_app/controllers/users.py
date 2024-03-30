from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request

@app.route("/")
@app.route("/users")
def index():
    users = User.find_all()
    return render_template("index.html", users=users)


@app.route("/users/new_user")
def new_user():
    return render_template("new_user.html")


@app.post("/users/create")
def create_user():
    print(request.form)
    user_id = User.create(request.form)
    print("THIS IS THE NEW USER'S ID:" + str(user_id))
    return redirect("/users")


@app.get("/users/<int:user_id>")
def user_details(user_id):
    user = User.find_by_id(user_id)
    if user == None:
        return "Cannot find user."
    
    return render_template("user_details.html", user=user)

@app.get("/users/<int:user_id>/edit")
def edit_user(user_id):
    user = User.find_by_id(user_id)
    if user == None:
        return "Cannot find user."
    return render_template("edit_user.html", user=user)

@app.post("/users/update")
def update_user():
    user_id = request.form["user_id"]
    User.update(request.form)
    return redirect(f"/users/{user_id}")

@app.post("/users/<int:user_id>/delete")
def  delete_user(user_id):
    User.delete_by_id(user_id)
    return redirect("/users")
