# from flaskapp.api.routes import main
from flask import Flask
from flaskapp.config import Config
from flask_restful import Api
from flaskapp.api.tables import Admin, db
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import random
from flask_jwt_extended import JWTManager

# created the instances
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    # Init the instances
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # init blueprints
    # from flaskapp.api.routes import main
    from flaskapp.api.routes import back

    # app.register_blueprint(main)  # linking blueprint main in the main/routes
    app.register_blueprint(back)  # linking blueprint api in api/routes

    # with app.app_context():
    #     db.session.add(
    #         Admin(
    #             id=random.randint(10000, 100000),
    #             username="krishnag+02@gmail.com",
    #             password=bcrypt.generate_password_hash("test1234")
    #         )
    #     )
    #     db.session.commit()
    return app
