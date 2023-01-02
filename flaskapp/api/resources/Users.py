from email import message
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort
import pandas as pd
import random
import json
from flaskapp.api.tables import db, User
from flaskapp import bcrypt, jwt
from flaskapp.api.alchemy_encoder import AlchemyEncoder
from flask_bcrypt import generate_password_hash
from flask_jwt_extended import jwt_required


class Users(Resource):
    def __init__(self):
        # this defines the structure of the resource.
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'user_id', type=int, help="User id is missing")
        self.reqparse.add_argument(
            'username', type=str, help="Username desc missing")
        self.reqparse.add_argument(
            'password', type=str, help="password is missing")
        self.reqparse.add_argument(
            'avatar', type=str, help="avatar is missing")

    def post(self):
        args = self.reqparse.parse_args()
        random_id = random.randint(10000, 100000)
        db.session.add(
            User(
                user_id=int(random_id),
                username=args['username'],
                password=bcrypt.generate_password_hash(args['password']),
                avatar=args['avatar'],
            )
        )
        db.session.commit()
        return random_id

    def get(self, user_id=None):
        user = {}
        if user_id:
            user = json.loads(json.dumps(User.query.filter_by(
                user_id=int(user_id)).first(), cls=AlchemyEncoder))
            return user
        else:
            return ("User not found")

    def put(self):
        args = self.reqparse.parse_args()
        user = {}
        user = User.query.filter_by(user_id=int(args['user_id'])).first()
        if bcrypt.check_password_hash(user.password, args['password']):
            if args['avatar']:
                user.avatar = args['avatar']
            if args['password']:
                user.password = args['password']
        else:
            abort(404, message="Password is incorrect")
        db.session.commit()

    def delete(self):
        args = self.reqparse.parse_args()
        delete_user_id = int(args['user_id'])
        User.query.filter_by(user_id=delete_user_id).delete()
        db.session.commit()
