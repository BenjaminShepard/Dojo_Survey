from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "ec3b1c3e3f09ed1879eb548401ac8a59113529f6d35aef512a7efc3f0c7b14f8"


@app.route("/")
def index():
    """The route that displays the form"""
    return render_template("index.html")


@app.post("/process")
def process():
    """THe route that processes the form."""
    print("USERNAME:", request.form["username"])
    print("EMAIL:", request.form["email"])

    session["username"] = request.form["username"]
    session["email"] = request.form["email"]
    return redirect("/results")


@app.get("/results")
def results():
    """This is the route that displays the results"""
    print(session["username"])
    print(session["email"])
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True)
