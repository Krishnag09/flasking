from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import random

app = Flask(__name__)
api = Api(app)

actions = pd.read_excel('actions.xlsx')
actions = actions.set_index('action_id').T.to_dict()

@app.route("/")
@app.route("/home")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about-us")
def about_us():
    return "<p>This is About you!!</p>"

class Posts(Resource):
    def __init__(self):
        # this defines the structure of the resource.
        self.reqparse = reqparse.RequestParser() 
        self.reqparse.add_argument('action_id', type=int, help= "Action id is missing")
    def get(self, action_id= None): 
        #  defines how the get statement works with the particular resource.
        if not action_id:
            return jsonify(actions)
        if "," in str(action_id):
            actionids = action_id.split(",")
            action = {}
            for id in actionids:
                print(id)
                action[int(id)]=actions[int(id)]
            return jsonify(action)
        else:
            action ={}
            action[int(action_id)] = actions[int(action_id)]
            return jsonify(action)
class NewPosts(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument('title', type=str, help = "action desc missing")
        self.reqparse.add_argument('description', type=str, help="action image is missing")
        self.reqparse.add_argument('impact', type=str, help="action impact is missing")
        self.reqparse.add_argument('image', type=str, help= "action title is missing")
        self.reqparse.add_argument('category', type=str, help= "forgot the category?")

    def post(self):
        args= self.reqparse.parse_args()

        action_info = { 
            "action_title": args['title'], 
            "action_description": args['description'], 
            "action_impact": args['impact'],
            "action_image": args['image'],
            "category": args['category']
            }
        id = random.randint(10000,100000)
        actions[id] = action_info
        return id

api.add_resource(NewPosts, '/api/newpost')
api.add_resource(Posts,'/api/posts', '/api/posts/<action_id>')

if __name__ == '__main__':
    app.run(debug=True)

# GET ALL POSTS http://127.0.0.1:5000/api/posts
# GET POST BY ID http://127.0.0.1:5000/api/posts/action_id
# GET MULTIPLE POSTS http://127.0.0.1:5000/api/posts/action_id1,action_id12