from flask import Blueprint
from flask_restful import Api



back = Blueprint('api', __name__)


api = Api(back)
from flaskapp.api.resources.Posts import Posts

api.add_resource(Posts,'/api/posts', '/api/posts/<action_id>')


# GET ALL POSTS methods http://127.0.0.1:5000/api/posts + method + args