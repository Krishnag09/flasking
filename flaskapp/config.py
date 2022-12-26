from distutils.command.config import config
import json
with open('/Users/krishnagaurav/flaskBackend/flaskapp/config.json') as config_file:
    config = json.load(config_file)


class Config:
    SECRET_KEY = config.get("SECRET_KEY")

    MAIL_PORT = ""
    DATABASE_INFORMATION = ""
    JWT_SECRET_KEY = config.get("JWT_SECRET_KEY")

    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:%slocalhost/api" % config.get("DATABASE_USER_PASSWORD")

    SQLALCHEMY_DATABASE_URI = "sqlite:////Users/krishnagaurav/flaskBackend/flaskapp/sqlite/test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = "Content-Type"
