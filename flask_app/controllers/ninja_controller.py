
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

from flask import render_template, redirect, request, session
from flask_app.__init__ import app

# home page
@app.route("/ninjas")
def new_ninjas():
    all_dojos = Dojo.get_all_dojos()

    return render_template("add_ninja.html",all_dojos = all_dojos)

@app.route("/ninjas",methods = ["post"])
def add_ninjas():

    return redirect("/dojos")


'''@app.route("/new/dojo")
def display_new_dojo():
    return render_template("add_dojo.html")

@app.route("/new/dojo",methods = ["post"])
def new_dojo():
    data = {
        "name":request.form["name"]
    }
    Dojo.add_dojo(data)
    return redirect("/")

@app.route("/show/<num>")
def display_dojo(num):
    data = {
        'id': num
    }
    curent_dojo = Dojo.get_one_user(data)
    return render_template("show_dojos.html",dojo=curent_dojo)'''
