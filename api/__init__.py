from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api

app = Flask(__name__)
app.config.from_object("connection")

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)

# IMPORTA as models e views para o migrate ver
from api.model import usuario_model

from api.views import usuario_view