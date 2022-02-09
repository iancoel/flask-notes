from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
# this function will run whenever we go to the / route
def home():
  return "<h1>Test</h1>"