from flask_restful import Resource
from api.schemas import usuario_schema
from flask import request, jsonify, make_response
from api.entities import usuario
from api.services import usuario_service
from api import api

class UsuarioList(Resource):
    def get(self):
        
        result = usuario_service.listar_usuario()
        if not result:
            return make_response(jsonify({"message": "Não existe usuarios"}), 404)
        return make_response(jsonify(result), 200)

    def post(self):
        
        us = usuario_schema.UsuarioSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            email = request.json['emailResource']
            senha = request.json['senha']

            usuario_novo = usuario.Usuario(nome, email, senha)
            result = usuario_service.cadastrar_usuario(usuario_novo)
    
            return make_response(jsonify(result), 201)


api.add_resource(UsuarioList, '/usuario')