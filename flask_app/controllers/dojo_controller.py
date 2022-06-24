
from flask_app.models.dojo_model import Dojo
from flask import render_template, redirect, request, session
from flask_app.__init__ import app
from flask_app.models.ninja_model import Ninja


# home page
@app.route("/")
@app.route("/dojos")
def display_all_dojos():
    all_dojos = Dojo.get_all_dojos()
    return render_template("all_dojos.html",all_dojos= all_dojos)


#to add a new dojo
@app.route("/new/dojo")
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
    curent_dojo = Dojo.get_one_ninja(data)
    return render_template("show_dojos.html",dojo = curent_dojo)

@app.route("/new/ninja", methods = ["post"])
def new_ninja():
    data = {
        "first_name":request.form["first_name"],
        "last_name": request.form["last_name"],
        "age":request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.add_ninja(data)
    return redirect("/")




'''
@app.route('/show/<int:user_id>')
# the parameter that you have here  has to mach on the url and inside of the dictionary
def show_one_user(user_id):
    data={
        'id': user_id
    }
    curent_user = Users.get_one_user(data)
#here we are just renaming the variable that we made before
    return render_template("show.html", user = curent_user)


@app.route("/edit/<int:num>")
def edit_one_user(num):
    data = {
        'id': num
    }
    user = Users.get_one_user(data)
    return render_template("edit.html" ,user = user)

@app.route("/edit/one_user/<int:num>",methods = ['post'])
def update_one_user_form(num):
    data = {
    'id': num,
    'first_name':request.form['first_name'],
    'last_name':request.form['last_name'],
    'email':request.form['email']
    }
    Users.update_one_user(data)
    return redirect("/users")

@app.route("/user/delete/<int:num>")
def delete_user(num):
    data = {
        "id": num
    }
    Users.delete_user(data)
    return redirect("/users")
'''