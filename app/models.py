from app import app
from app.forms import RegistrationForm
from flask import render_template

@app.route('/register')
def regestration():
    forms=RegistrationForm()
    return render_template('regestration.html', title='regestration', form=forms)
