
class ContaBancaria:
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def exibirSaldo(self):
        print(f"Conta {self.numero} - Titular: {self.titular}")

    def depositar(self, quantia):
        if quantia > 0:
            self.saldo += quantia
            print(f"Depósito de R$ {quantia:.2f} realizado.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self,quantia):
        if quantia >= self.saldo:
            self.saldo -= quantia
            print(f"Saque de R${quantia:.2f} realizado!")
        else:
            print(f"Saldo insuficiente.") 

    def transferir(self, quantia, outra_conta):
        if quantia <= 0:
            print("Valor de transferência inválido.")
        elif quantia <= self.saldo:
            self.saldo -= quantia
            outra_conta.depositar(quantia)
            print(f"Transferência de R$ {quantia:.2f} realizada.")
        else:
            print("Saldo insuficiente.")


def menu():
    print("=======================================")
    print("Opções:")
    print("1- Sacar")
    print("2- Depositar")
    print("3- Transferir")
    print("4- Exibir saldo")
    print("5- Sair")
    print("=======================================")

def main():
    conta1 = ContaBancaria("Larissa",1000)
    conta2 = ContaBancaria("Fulano", 500)

    while True:
        menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            valor = float(input("Digite o valor a ser sacado: "))
            conta1.sacar(valor)
        elif opcao == 2:
            valor = float(input("Digite o valor a ser depositado: "))
            conta1.depositar(valor)
        elif opcao == 3:
            valor = float(input("Digite o valor a ser transferido: "))
            conta1.transferir(valor, conta2)
        elif opcao == 4:
            conta1.exibirSaldo()
        elif opcao == 5:
            print("Encerrando...")
            break
        else:
            print("Opção inválida, tente novamente...")

main()


