from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError
# from  app.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3 , max=10)])
    email =StringField("Email", validators=[DataRequired(), Email()])
    password=PasswordField("Password", validators=[DataRequired()])
    confirm_password= PasswordField("Confirm Password", validators=[DataRequired(),EqualTo('password')])
    submit =SubmitField("Sign In")


    # def validate_username(self ,username):
    #     user=User.query.filter_by(username=username.data).first()
    #     if user is not None:
    #         raise ValidationError('Username exist')

    # def validate_email(self, email):
    #     user=User.query.filter_by(email=email.data).first()
    #     if user is not None:
    #         raise ValidationError('Email exist')




class LoginForm(FlaskForm):
    email =StringField("Email", validators=[DataRequired(), Email()])
    password= PasswordField("Password", validators=[DataRequired()])
    remember=BooleanField("Remember me?")
    submit=SubmitField("Login in")

class EditUserProfile(FlaskForm):
    username=StringField('Username' ,validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')



class newPostForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    body=TextAreaField('Pitch', validators=[DataRequired()])
    submit= submit=SubmitField("Submit")