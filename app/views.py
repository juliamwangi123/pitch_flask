import email
from turtle import title
from app import app
from app.forms import RegistrationForm,LoginForm
from flask import render_template,redirect,url_for,request,flash
from flask_login import current_user, login_user
from app.models import User
from app.route import index
from flask_login import logout_user


@app.route('/register', methods=['GET','POST' ])
def regestration():
    
    forms=RegistrationForm()
    
    return render_template('regestration.html', title='regestration', form=forms)


@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))