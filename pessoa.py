class Pessoa:
    def __init__(self, nome,idade):
        self._nome_da_pessoa = nome
        self._idade_da_pessoa = idade
        
    @property
    def nome(self):
        return self._nome_da_pessoa
    
    @nome.setter
    def nome(self, valor):
        self._nome_da_pessoa = valor
    
    @property
    def idade(self):
        return self._idade_da_pessoa
    
    @idade.setter
    def idade(self, valor):
        self._idade_da_pessoa = valor
    
while True:
    nome = input('Digite o nome : ')
    idade = input('Digite a idade: ')
    pessoa = Pessoa(nome, idade)
    print(vars(pessoa))
    parar = input('para parar digite [P]').upper().strip()
    if parar == 'P':
        break