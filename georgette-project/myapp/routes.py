from flask import Blueprint, redirect, request, url_for

from .extensions import db
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.all()
    users_list_html = [
        f"<li>{user.username}, {user.dob}, {user.gender}, {user.number}, {user.classOfUser}</li>" 
        for user in users
    ]
    return f"<ul>{''.join(users_list_html)}</ul>"

@main.route('/add', methods=['POST'])
def add_user():
    username = request.form['username']
    dob = request.form['dob']
    gender = request.form['gender']
    number = request.form['number']
    classOfUser = request.form['classOfUser']
    
    new_user = User(username=username, dob=dob, gender=gender, number=number, classOfUser=classOfUser)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for("main.index"))
