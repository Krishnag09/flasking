from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort
from flaskapp.api.tables import db, Admin
from flaskapp.api.alchemy_encoder import AlchemyEncoder
from datetime import timedelta
from flask_jwt_extended import create_access_token, jwt_required
from flask_bcrypt import check_password_hash


class Login(Resource):

    def __init__(self):
        # this defines the structure of the resource.
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username', type=str, help="Username desc missing")
        self.reqparse.add_argument(
            'password', type=str, help="password is missing")

    def post(self):
        args = self.reqparse.parse_args()
        admin_user = Admin.query.filter_by(
            username=args['username']).first()
        print("hello", admin_user)
        if admin_user and check_password_hash(admin_user.password, args['password']):
            access_token = create_access_token(identity=str(
                admin_user.id), expires_delta=timedelta(hours=7))
            return {'token': access_token}, 200
        else:
            return {'error': 'username or password is invalid'}, 401
