from flask_restful import Resource
from marshmallow import ValidationError
from api.schemas import usuario_schema
from flask import request, jsonify, make_response
from api.entities import usuario
from api.services import usuario_service
from api import api

class UsuarioList(Resource):
    def get(self):
        
        # NOTE: esse ponto foi atualizado para o uso do schema
        usuarios = usuario_service.listar_usuario()
        if not usuarios:
            return make_response(jsonify({"message": "Não existe usuarios"}), 404)
        
        schema = usuario_schema.UsuarioSchema(many=True)
        return make_response(jsonify(schema.dump(usuarios)), 200)

    def post(self):
        # NOTE validação da serialização, alteração de if else para try e except, 
        # verifica se o usuario ja existe

        schema = usuario_schema.UsuarioSchema()

        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)
        
        if usuario_service.listar_usuario_email(dados['email']):
            return make_response(jsonify({"message": "Email já cadastrado"}), 400)
        
        
        try:
            # como estamos validando os dados, vamos buscar os dados da variavel 'dados' depois da serialização
            novo_usuario = usuario.Usuario(
            nome = dados['nome'],
            email = dados['email'],
            senha = dados['senha'])

            resultado = usuario_service.cadastrar_usuario(novo_usuario)
            return make_response(jsonify(schema.dump(resultado)), 201)


        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)



api.add_resource(UsuarioList, '/usuario', '/usuario/<int:id_usuario>') # /usuario/1