"""nome = 'diego'
print(type(nome)) #imprime class 'str' - classe do tipo string
print(nome.upper())"""#CTRL+clicar com botão direito em cima do metodo UPPER
#exemplo de uma classe para minha TV
"""class TV():
    cor = 'preta' #atributos
    tamanho = 55
    volume = 30
    def liga_desliga(self): #function/métodos
        pass
    def mudar_canal(self):
        pass
    def mudar_volume():
        pass
#chamando meus metodos
TV.liga_desliga()
TV.mudar_voluma()
TV.mudar_canal()"""
#Criar uma classe para PESSOA
"""class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
#criando instâncias da classe Pessoa
pessoa1 = Pessoa("Diego",30)
pessoa2 = Pessoa("Joao",50)
#acessando atributos das instâncias
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa2.nome)
print(pessoa2.idade)"""
#Criar uma classe para livro
"""class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def detalhes(self):
        return (f"{self.titulo} escrito por {self.autor}, com {self.paginas} páginas.")
#criando a instância da classe livro
livro1 = Livro("Dom casmuro","Machado de Assis",300)
print(livro1.detalhes())"""
#Criar uma classe ContaBancaria
#funcao (def) __init__ + funcao depositar + funcao sacar + funcao saldo


"""class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0): 
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self,quantia):
        self.saldo += quantia

    def sacar(self,quantia):
        if quantia <= self.saldo:
            self.saldo -= quantia
        else:
            print(f"Saldo insuficiente, seu saldo {self.saldo}")    

    def obter_saldo(self):
        return self.saldo
    
    def trasnferir(self,outra_conta,quantia):
        if quantia <= self.saldo:
            self.saldo -= quantia
            outra_conta.depositar(quantia)
        else:
            print(f"Saldo insuficiente, seu saldo é: {self.saldo}") 
    

#exemplo de uso, criando a instância da classe
conta1 = ContaBancaria("Diego",1000)
conta2 = ContaBancaria("Fulano", 500)
print(f"{conta1.titular} seu saldo atual R${conta1.obter_saldo()}")
print(f"{conta2.titular} seu saldo atual R${conta2.obter_saldo()}")

#tentar sacar mais que saldo
#conta1.sacar(1500)
#conta2.sacar(600)

#Fazendo um deposito na conta
conta1.depositar(500)
conta2.depositar(300)
print(f"{conta1.titular} seu novo saldo atual R${conta1.obter_saldo()}")
print(f"{conta2.titular} seu novo saldo atual R${conta2.obter_saldo()}")

#Transferindo para outra conta
conta1.trasnferir(conta2,2000)
conta2.trasnferir(conta1,300)
"""