import email
from flask_login import current_user, login_user , logout_user 
from app import app
from .forms import  RegistrationForm, LoginForm
from flask import render_template, request,flash,redirect,url_for,request
from app.models import User 
from werkzeug.urls import url_parse
from app import db


from flask_login import login_required

#this oute lead to home page and one can only view it when logged in
@app.route('/')
@app.route('/index')
@login_required
def index():

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', posts=posts)




#this route leads to  user profile page and also requires user to login first
@app.route('/profile/<username>')
@login_required
def profile(username):
    user=User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('profile.html', user=user, posts=posts)



@app.route('/register', methods=['GET','POST' ])
def regestration():
    
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=RegistrationForm()

    if request.method == "POST" and form.validate_on_submit():
        user=User(username=form.username.data, email=form.email.data)
        user.set_password(password=form.password.data)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created succesufully for {form.username.data}!', 'success')
        return redirect(url_for('login'))
   
    return render_template('regestration.html' ,form=form, title="Register")

    


@app.route('/login' , methods=['GET','POST' ])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(f'Invalid username or password', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc !='':
            next_page=url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form, title='Login')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))