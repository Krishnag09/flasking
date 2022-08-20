from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import random
import json
from flaskapp.api.tables import db, User
from flaskapp.api.alchemy_encoder import AlchemyEncoder

class Users(Resource):
    def __init__(self):
        # this defines the structure of the resource.
        self.reqparse = reqparse.RequestParser() 
        self.reqparse.add_argument('user_id', type=int, help= "User id is missing")
        self.reqparse.add_argument('username', type=str, help = "Username desc missing")
        self.reqparse.add_argument('password', type=str, help="password is missing")
        self.reqparse.add_argument('avatar', type=str, help="avatar is missing")


    def post(self):
        args= self.reqparse.parse_args()
        random_id = random.randint(10000,100000)
        db.session.add(
            User(
                user_id = int(random_id), 
                username = args['username'],
                password = args['password'],
                avatar = args['avatar'],
            )
        )
        db.session.commit()
        return random_id




