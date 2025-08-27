# livro_resource.py

from flask import request, jsonify, make_response
from flask_restful import Resource
from marshmallow import ValidationError
from model.livro import Livro
from services import livro_service
from schemas import livro_schema

# para trabalhar com todos os livros
class LivroList(Resource):
    def get(self):
        livros = livro_service.listar_livros()
        if not livros:
            return make_response(jsonify({"message": "Não há livros cadastrados"}), 404)
        
        schema = livro_schema.LivroSchema(many=True)
        return make_response(jsonify(schema.dump(livros)), 200)

    def post(self):
        schema = livro_schema.LivroSchema()
        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)
        
        try:
            novo_livro = Livro(
                titulo=dados['titulo'],
                autor=dados['autor'],
                ano=dados['ano'],
                isbn=dados['isbn']
            )
            resultado = livro_service.cadastrar_livro(novo_livro)
            return make_response(jsonify(schema.dump(resultado)), 201)
        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)

# para trabalhar com um livro específico
class LivroResource(Resource):
    def get(self, id_livro):
        livro = livro_service.listar_livro_id(id_livro)
        if livro:
            schema = livro_schema.LivroSchema()
            return make_response(jsonify(schema.dump(livro)), 200)
        return make_response(jsonify({"message": "Livro não encontrado"}), 404)

    def put(self, id_livro):
        schema = livro_schema.LivroSchema()
        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)
        
        livro = livro_service.editar_livro(id_livro, dados)
        if livro:
            return make_response(jsonify(schema.dump(livro)), 200)
        return make_response(jsonify({"message": "Livro não encontrado"}), 404)

    def delete(self, id_livro):
        if livro_service.excluir_livro(id_livro):
            return make_response(jsonify({"message": "Livro excluído com sucesso"}), 200)
        return make_response(jsonify({"message": "Livro não encontrado"}), 404)

# no seu app principal:
api.add_resource(LivroList, '/livros')
api.add_resource(LivroResource, '/livros/<int:id_livro>')
