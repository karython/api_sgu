from ..model import usuario_model
from ..schemas.usuario_schema import UsuarioSchema
from api import db 

def cadastrar_usuario(usuario):
    usuario_db = usuario_model.Usuario(nome =usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario_db.gen_senha(usuario.senha)
    db.session.add(usuario_db)
    db.session.commit()
    return usuario_db
    

def listar_usuario():
    usuarios = usuario_model.Usuario.query.all()
    schema = UsuarioSchema(many=True)
    return usuario_model.Usuario.query.all()

def listar_usuario_email(email):
    return usuario_model.Usuario.query.filter_by(email = email).first()

def excluir_usuario(id):
    usuario = usuario_model.Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return True
    return False

def editar_usuario(id, novo_usuario):
    usuario = usuario_model.Usuario.query.get(id)
    if usuario:
        usuario.nome = novo_usuario.nome
        usuario.email = novo_usuario.email
        if novo_usuario.senha:
            usuario.gen_senha(novo_usuario.senha)
        db.session.commit()
        return usuario
    return None
    
# NOTE: função adicionada para listar usuario por ID
def listar_usuario_id(id):
    try:
        # busca o usuario pelo ID no banco de dados
        usuario_encontrado = usuario_model.Usuario.query.get(id)
        return usuario_encontrado
    except Exception as e:
        print(f"Erro ao listar usuario por ID: {e}")
        return None