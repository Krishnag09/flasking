from email import message
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort
import pandas as pd
import random
import json
from flaskapp.api.tables import db, Content,User
from flaskapp.api.alchemy_encoder import AlchemyEncoder
from flaskapp import bcrypt

class Likes(Resource):
    def __init__(self):
        # this defines the structure of the resource. 
        self.reqparse = reqparse.RequestParser() 
        self.reqparse.add_argument('user_id', type=int, help= "User id is missing")
        self.reqparse.add_argument('action_id', type=int, help = "Action id desc missing")
        self.reqparse.add_argument('likes', type=bool, help="Likes data is missing")

    def post(self):
        args= self.reqparse.parse_args()
        random_id = random.randint(10000,100000)
        action_id = args['action_id']
        user_id = args['user_id']
        likes = args['likes']
        post = Content.query.filter_by(action_id=int(action_id)).first()
        user =  User.query.filter_by(user_id = int(user_id)).first()

        if action_id and user_id:

            print(post)
            if likes:
                post.rating +=1
            else:
                post.rating -=1
        db.session.commit()





