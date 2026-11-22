from flask import Blueprint
from flask import render_template


views = Blueprint('views', __name__)

@views.route('/')
def home():
    print("Home route executed")
    return render_template("home.html")


@views.route('/sudoku/<difficulty>')
def sudokupage(difficulty):

    return render_template("sudokupage.html", difficulty=difficulty)

@views.route('/solver')
def solverpage():

    return render_template("explain.html")
