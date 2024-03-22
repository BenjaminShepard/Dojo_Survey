from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep this a secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect ("/results")

@app.route("/results")
def result():
    return render_template(
        "result.html",
        name=session["name"],
        location=session["location"],
        lang=session["language"],
        comments=session["comments"],
    )

@app.route("/reset", methods=["GET"])
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)