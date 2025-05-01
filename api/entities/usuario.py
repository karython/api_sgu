

class Usuario:
    def __init__(self,nome,email,senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    #metodo get
    @property
    def nome(self):
        return self.__nome
    
    #metado set
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    #metodo get
    @property
    def email(self):
        return self.__email
    
    #metado set
    @email.setter
    def email(self,email):
        self.__email = email

    #metodo get
    @property
    def senha(self):
        return self.__senha
    
    #metado set
    @senha.setter
    def senha(self,senha):
        self.__senha = senha
    

""" if __name__== '__main__':   
    gomes = Usuario('gomes','gomes@gmail.com','1234')
    print(gomes.nome)
    print(gomes.email) """

""" class caracteristicas(Usuario): 
    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)
        self.__caracteristicas = caracteristicas

    @property
    def caracteristicas(self):
        return self.__caracteristicas """