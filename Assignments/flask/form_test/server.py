from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'this is our temporary secret key' #never use a secret key this easy

@app.route('/')
def index():
    return render_template("index.html")

@app.post('/users')
def create_user():
    print('Got Post info')
    print(request.form)
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

#adding this method
@app.route("/show")
def show_user():
    return render_template('show.html')

if __name__ == '__main__':
    app.run(debug=True)