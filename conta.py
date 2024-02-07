class Conta:
    def __init__(self, agencia, numero_conta, saldo):
        self._agencia = agencia
        self._conta = numero_conta
        self._saldo = saldo
    
    def deposito(self, valor):
        valor = input('Valor do deposito: ')
        self._saldo += valor 
        return  self._saldo
    
    def sacar(self,valor):
        valor = ('Digite o valor a sacar: ')
        if valor>self._saldo:
            print('Sem saldo suficiente')
        else: 
            self._saldo -= valor
        return self._saldo
    


    



        

    # ok - Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    # ok - ContaCorrente deve ter um limite extra
    # ok - Contas têm agência, número da conta e saldo
    # ok -Contas devem ter método para depósito
    # ok - Conta (super classe) deve ter o método sacar abstrato (Abstração e
    # polimorfismo - as subclasses que implementam o método sacar)