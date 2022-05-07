from turtle import title
from app import app
from app.forms import RegistrationForm,LoginForm
from flask import render_template

@app.route('/register')
def regestration():
    forms=RegistrationForm()
    return render_template('regestration.html', title='regestration', form=forms)
@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html', title='login', form=form)
