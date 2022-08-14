from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd

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
    
api.add_resource(Posts,'/api/posts', '/api/posts/<action_id>')

if __name__ == '__main__':
    app.run(debug=True)
