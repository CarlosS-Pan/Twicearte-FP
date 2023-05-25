from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():  # put application's code here
    return render_template('login.html')
