# Simulando banco com lista
livros = []
contador_id = 1

def listar_livros():
    return livros

def listar_livro_id(id_livro):
    return next((livro for livro in livros if livro.id == id_livro), None)

def cadastrar_livro(livro):
    global contador_id
    livro.id = contador_id
    livros.append(livro)
    contador_id += 1
    return livro

def editar_livro(id_livro, dados):
    livro = listar_livro_id(id_livro)
    if livro:
        livro.titulo = dados.get('titulo', livro.titulo)
        livro.autor = dados.get('autor', livro.autor)
        livro.ano = dados.get('ano', livro.ano)
        livro.isbn = dados.get('isbn', livro.isbn)
        return livro
    return None

def excluir_livro(id_livro):
    global livros
    livro = listar_livro_id(id_livro)
    if livro:
        livros = [l for l in livros if l.id != id_livro]
        return True
    return False
