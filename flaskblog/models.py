from datetime import datetime
from flaskblog import db, login_manager, admin
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView
from flask import abort, session
from flask_admin.menu import MenuLink


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.DateTime)
    add = db.Column(db.String(120), nullable=False)
    phn = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.email}')"


class SecureModelView(ModelView):
    column_searchable_list = (User.fname, User.lname, User.add)

    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)


# class MyModelView(ModelView):


admin.add_view(SecureModelView(User, db.session))
admin.add_link(MenuLink(name='Logout', category='', url="/logout"))
