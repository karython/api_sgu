class Livro:
    def __init__(self, titulo, autor, ano, isbn):
        self.id = None  # ID será atribuído ao salvar no banco
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn
