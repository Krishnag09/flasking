from flaskapp.api.resources.Login import Login
from flaskapp.api.resources.Likes import Likes
from flaskapp.api.resources.Users import Users
from flaskapp.api.resources.Posts import Posts
from flask import Blueprint
from flask_restful import Api


back = Blueprint('api', __name__)
api = Api(back)

# class to execute when the route is hit

api.add_resource(Login, '/api/auth/login',)
api.add_resource(Users, '/api/users', '/api/users/<user_id>')
api.add_resource(Posts, '/api/posts', '/api/posts/<action_id>')
api.add_resource(Likes, '/api/likes')


# GET ALL POSTS methods http://127.0.0.1:5000/api/posts + method + args
