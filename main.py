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
        self.reqparse.add_argument('action_title', type=str, help = "action desc missing")
        self.reqparse.add_argument('action_description', type=str, help="action image is missing")
        self.reqparse.add_argument('action_impact', type=str, help="action impact is missing")
        self.reqparse.add_argument('action_image', type=str, help= "action title is missing")
        self.reqparse.add_argument('category', type=str, help= "forgot the category?")

    def get(self, action_id= None): 
        #  defines how the get statement works with the particular resource.
        if not action_id:
            return jsonify(actions)
        if "," in str(action_id):
            actionids = action_id.split(",")
            action = {}
            for id in actionids:
                if id not in actions:
                    return(id, "not found")
                else:
                    action[int(id)]=actions[int(id)]
            return jsonify(action)
        else:
            action ={}
            action[int(action_id)] = actions[int(action_id)]
            return jsonify(action)

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

    def put(self):
        args = self.reqparse.parse_args()
        action_id= int(args['action_id'])
        new_title = args['action_title']
        new_desc = args['action_description']
        
        if new_title:
            actions[action_id]['action_title']=new_title
        if new_desc:
            actions[action_id]['action_description']=new_desc
        # can you make it better
        return actions[action_id]

    def delete(self):
        args = self.reqparse.parse_args()
        print (args)
        delete_action_id= int(args['delete_action_id'])
        print (delete_action_id)
        if(delete_action_id in actions):
            actions.pop(int(args['delete_action_id']))
            return(delete_action_id,"was Popped")
        else:
            return("delete id is not present")

api.add_resource(Posts,'/api/posts', '/api/posts/<action_id>')

if __name__ == '__main__':
    app.run(debug=True)

# GET ALL POSTS methods http://127.0.0.1:5000/api/posts + method + args
