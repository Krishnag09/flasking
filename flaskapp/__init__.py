from flask import Flask
from flaskapp.config import Config
from flask_restful import Api
from flaskapp.api.tables import db

#created the instances
api = Api()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    #Init the instances
    db.init_app(app)

    #init blueprints
    from flaskapp.main.routes import main
    from flaskapp.api.routes import back

    app.register_blueprint(main) # linking blueprint main in the main/routes
    app.register_blueprint(back) # linking blueprint api in api/routes

    return app
