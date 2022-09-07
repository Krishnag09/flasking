from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import random
import json
from flaskapp.api.tables import db, Content
from flaskapp.api.alchemy_encoder import AlchemyEncoder
from flask_jwt_extended import jwt_required


class Posts(Resource):
    def __init__(self):
        # this defines the structure of the resource.
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'action_id', type=int, help="Action id is missing")
        self.reqparse.add_argument(
            'action_title', type=str, help="action desc missing")
        self.reqparse.add_argument(
            'action_description', type=str, help="action image is missing")
        self.reqparse.add_argument(
            'action_impact', type=str, help="action impact is missing")
        self.reqparse.add_argument(
            'action_image', type=str, help="action title is missing")
        self.reqparse.add_argument(
            'category', type=str, help="forgot the category?")
        self.reqparse.add_argument(
            'delete_action_id', type=str, help="we need the id for delete item")

    @jwt_required()
    def get(self, action_id=None):
        actions = json.loads(json.dumps(
            Content.query.all(), cls=AlchemyEncoder))
        actions = {action["action_id"]: action for action in actions}
        #  defines how the get statement works with the particular resource.
        if not action_id:
            return actions
        if "," in str(action_id):
            actionids = action_id.split(",")
            action = {}
            for id in actionids:
                action[int(id)] = json.loads(json.dumps(
                    Content.query.filter_by(action_id=int(id)).all(), cls=AlchemyEncoder))
            return action
        else:
            action = {}
            action[int(action_id)] = json.loads(json.dumps(
                Content.query.filter_by(action_id=action_id).first(), cls=AlchemyEncoder))
            return action

    @jwt_required()
    def post(self):
        args = self.reqparse.parse_args()
        random_id = random.randint(10000, 100000)
        db.session.add(
            Content(
                action_id=int(random_id),
                action_title=args['title'],
                action_description=args['description'],
                action_impact=args['impact'],
                action_image=args['image'],
                category=args['category'],
                rating=0,
                comments="{}".format({}),
            )
        )
        db.session.commit()
        return id

    @jwt_required()
    def put(self):
        actions = json.loads(json.dumps(
            Content.query.all(), cls=AlchemyEncoder))
        actions = {action["action_id"]: action for action in actions}
        args = self.reqparse.parse_args()
        action_id = int(args['action_id'])
        new_title = args['action_title']
        new_desc = args['action_description']
        if new_title:
            actions[action_id]['action_title'] = new_title
        if new_desc:
            actions[action_id]['action_description'] = new_desc
        # can you make it better
        return actions[action_id]

    @jwt_required()
    def delete(self):
        args = self.reqparse.parse_args()
        delete_action_id = int(args['delete_action_id'])
        Content.query.filter_by(action_id=delete_action_id).delete()
        db.session.commit()
        return (delete_action_id)
