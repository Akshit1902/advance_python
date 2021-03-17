from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    fname = StringField('fname', validators=[DataRequired(),
                                             Length(min=2, max=20)])
    lname = StringField('lname', validators=[DataRequired(),
                                             Length(min=2, max=20)])

    dob = DateField('dob', format='%m/%d/%Y')
    add = StringField('Add', validators=[DataRequired()])
    phn = StringField('Phn', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                     EqualTo('password')])
    submit = SubmitField('Sign Up')

    # def fname(self, fname):
    #     user = User.query.filter_by(fname=fname.data).first()
    #     if user:
    #         raise ValidationError('That First Name is already taken')
    #
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# class UpdateAccountForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(),
#                                                    Length(min=2, max=20)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     submit = SubmitField('Update')
#
#     def validate_username(self, username):
#         if username.data != current_user.username:
#             user = User.query.filter_by(username=username.data).first()
#             if user:
#                 raise ValidationError('That username is already taken')
#
#     def validate_email(self, email):
#         if email.data != current_user.email:
#             user = User.query.filter_by(email=email.data).first()
#             if user:
#                 raise ValidationError('That email is already taken')


# class PostForm(FlaskForm):
#     title = StringField('Title', validators=[DataRequired()])
#     content = TextAreaField('Content', validators=[DataRequired()])
#     submit = SubmitField('Post')
