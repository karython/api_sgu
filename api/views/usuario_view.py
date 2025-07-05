from flask_restful import Resource
from marshmallow import ValidationError
from api.schemas import usuario_schema
from flask import request, jsonify, make_response
from api.model.usuario_model import Usuario
from api.services import usuario_service
from api import api

# para trabalhar com todos os usuários
class UsuarioList(Resource):
    def get(self):
        usuarios = usuario_service.listar_usuario()
        if not usuarios:
            return make_response(jsonify({"message": "Não existe usuarios"}), 404)
        
        schema = usuario_schema.UsuarioSchema(many=True)
        return make_response(jsonify(schema.dump(usuarios)), 200)

    def post(self):
        schema = usuario_schema.UsuarioSchema()
        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)
        
        if usuario_service.listar_usuario_email(dados['email']):
            return make_response(jsonify({"message": "Email já cadastrado"}), 400)
        
        try:
            novo_usuario = Usuario(
                nome=dados['nome'],
                email=dados['email'],
                senha=dados['senha']
            )
            novo_usuario.gen_senha(dados['senha'])
            resultado = usuario_service.cadastrar_usuario(novo_usuario)
            return make_response(jsonify(schema.dump(resultado)), 201)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)

api.add_resource(UsuarioList, '/usuarios')  # Rota única para listar/criar usuários

# para trabalhar com um usuário específico
class UsuarioResource(Resource):
    def get(self, id_usuario):
        usuario = usuario_service.listar_usuario_id(id_usuario)
        if usuario:
            schema = usuario_schema.UsuarioSchema()
            return make_response(jsonify(schema.dump(usuario)), 200)
        return make_response(jsonify({"message": "Usuário não encontrado"}), 404)

    def put(self, id_usuario):
        schema = usuario_schema.UsuarioSchema()
        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)
        
        usuario = usuario_service.editar_usuario(id_usuario, dados)
        if usuario:
            return make_response(jsonify(schema.dump(usuario)), 200)
        return make_response(jsonify({"message": "Usuário não encontrado"}), 404)

    def delete(self, id_usuario):
        if usuario_service.excluir_usuario(id_usuario):
            return make_response(jsonify({"message": "Usuário excluído com sucesso"}), 200)
        return make_response(jsonify({"message": "Usuário não encontrado"}), 404)

api.add_resource(UsuarioResource, '/usuarios/<int:id_usuario>')  # Rota única para operações específicas


