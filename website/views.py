from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
# this function will run whenever we go to the / route
def home():
  return render_template('home.html')