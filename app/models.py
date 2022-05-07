from turtle import title
from app import app
from app.forms import Regestration,Login
from flask import render_template

@app.route('/Register')
def regestration():
    forms=Regestration()
    return render_template('regestration.html', title='regestration', forms=forms)
