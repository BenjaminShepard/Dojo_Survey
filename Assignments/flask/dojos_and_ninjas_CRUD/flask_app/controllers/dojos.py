from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def all_dojos():
    dojos = Dojo.find_all()
    print(dojos)
    return render_template('index.html', dojos=dojos)

@app.post('/create_dojo')
def create_dojo():
    data = {"name": request.form["name"]}
    Dojo.create_dojo(request.form)
    return redirect('/')

@app.route('/dojoshow/<int:dojo_id>')
def dojoshow(dojo_id):
    data = {"id": id}
    return render_template('dojoshow.html', dojo = Dojo.find_all)


