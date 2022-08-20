
from unicodedata import category
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db=SQLAlchemy() 
class Content(db.Model):
    action_id = db.Column(db.Integer(), primary_key= True)
    action_title = db.Column(db.String(100))
    action_description = db.Column(db.Text(100))
    action_impact = db.Column(db.Text(150))
    action_image = db.Column(db.String(30))
    category= db.Column(db.String(20))
    rating = db.Column(db.Integer())
    comments = db.Column(db.Text(40))

    def __repr__(self):
        return '<Post %s>' % self.action_id

class User(db.Model):
    user_id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.Text(100))
    password = db.Column(db.Text(100))
    avatar = db.Column(db.Text(150))


    def __repr__(self):
        return '<User %s>' % self.user_id

