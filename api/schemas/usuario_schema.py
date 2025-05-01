from api.model import usuario_model
from api import ma
from marshmallow import fields

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = usuario_model.Usuario 

        fields = ('id', 'nome', 'email', 'senha')

    nome = fields.String(required=True)
    email = fields.Email(required=True)
    senha = fields.String(required=True)