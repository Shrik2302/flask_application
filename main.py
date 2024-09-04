import os
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for, redirect, session, flash
from forms import NameForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'flask form'
@app.route("/")
def index():
    return "<h1> Welcome to the flask </h1>"

@app.route("/<name>")
def user(name):
    return "<h1>welcome {}!</h1>".format(name)

@app.route("/request")
def index_req():
    user_agent = request.headers.get("user_agent")
    return "<h1>{}</h1>".format(user_agent)

@app.route("/user/<name>")
def user_name(name):
    url = url_for("index_req")

    return render_template("user.html", name=name, url=url)
    # user_list = ["shri", "mahesh", "vijay"]
    # return render_template("user.html", name=user_list)



@app.route("/macro")
def macro_func():
    my_list = [1,2,3,4,5,6]
    more_numbers = [11,22,33,44]
    return render_template("user.html", name="shrikant", numbers=my_list, more_numbers=more_numbers)

@ app.route('/user/form', methods=['GET', 'POST'])
def user_name_form():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name= form.name.data
        session['name'] = form.name.data
        form.name.data = ''
        basedir = os.path.abspath(os.path.dirname(__file__))
        print(basedir)
        return redirect(url_for('user', name=session['name']))
    return render_template("form.html", form=form, name=name)

