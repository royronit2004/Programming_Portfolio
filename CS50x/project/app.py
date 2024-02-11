#Final Project CS50

from cs50 import SQL
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


db = SQL("sqlite:///members.db")


TEAMS = [
    "Iron Man",
    "Captain America"
]

@app.route("/")
def index():
    return render_template("index.html", teams=TEAMS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    last = request.form.get("last")
    team = request.form.get("team")
    if not name or last or team not in TEAMS:
        return render_template("failure.html")



    db.execute("INSERT INTO members (name, last, team) VALUES(?, ?, ?)", name, last, team)


    user_input = request.form.get('team')

    if user_input == 'Iron Man':
        return redirect(url_for('ironman_page'))
    elif user_input == 'Captain America':
        return redirect(url_for('captain_page'))
    else:
        return render_template("failure.html")


@app.route('/ironman')
def ironman_page():
    return render_template('ironman.html')

@app.route('/captain')
def captain_page():
    return render_template('captain.html')


@app.route("/members")
def members():
    members = db.execute("SELECT * FROM members")
    return render_template("members.html", members=members)