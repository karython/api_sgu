from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object("connection")

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)
CORS(app)

# Inicializar o banco de dados
@app.before_request
def create_tables():
    if request.endpoint == 'index':  # Executar apenas na primeira requisição
        db.create_all()

# IMPORTA as views para o migrate ver
from .views import usuario_view
from .model import usuario_model