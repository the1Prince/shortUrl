from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key='5f4feabe-e605-4deb-944a-6940de13b5b5'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import routes, models