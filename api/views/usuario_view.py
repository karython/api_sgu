from flask_restful import Resource
from marshmallow import ValidationError
from api.schemas import usuario_schema
from flask import request, jsonify, make_response
from api.entities import usuario
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
    #TODO: implementar a busca por ID

    def post(self):

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
        


api.add_resource(UsuarioList, '/usuario')


# class UsuarioList(Resource): para editar e excluir usuários
class UsuarioResource(Resource):
    # função para buscar um usuário por ID
    def get(self, id_usuario):
        usuario_encontrado = usuario_service.listar_usuario_id(id_usuario)
        if not usuario_encontrado:
            return make_response(jsonify({"message": "Usuário não encontrado"}), 404)
        
        schema = usuario_schema.UsuarioSchema()
        return make_response(jsonify(schema.dump(usuario_encontrado)), 200)
    
    
    def put(self, id_usuario):
        usuario_encontrado = usuario_service.listar_usuario_id(id_usuario)
        if not usuario_encontrado:
            return make_response(jsonify({"message": "Usuário não encontrado"}), 404)
        
        schema = usuario_schema.UsuarioSchema()

        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)
        
        # atualiza os dados do usuário
        try:
            usuario_encontrado.nome = dados['nome']
            usuario_encontrado.email = dados['email']
            
            # faz a criptografia da senha antes de salvar no banco de dados
            if dados.get('senha'):
                usuario_encontrado.gen_senha(dados['senha'])

            usuario_service.editar_usuario(id_usuario, usuario_encontrado)
            return make_response(jsonify(schema.dump(usuario_encontrado)), 200)

        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)

    def delete(self, id_usuario):
        usuario_encontrado = usuario_service.listar_usuario_id(id_usuario)
        if not usuario_encontrado:
            return make_response(jsonify({"message": "Usuário não encontrado"}), 404)
        try:
            usuario_service.excluir_usuario(id_usuario)
            return make_response(jsonify({"message": "Usuário excluído com sucesso"}), 200)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)
        

api.add_resource(UsuarioResource, '/usuario/<int:id_usuario>')  # /usuario/1