class Conta:
    def __init__(self,numeroAgencia,saldo=0):
        self._saldo = saldo # _ torna ele privado
        self.numeroAgencia = numeroAgencia
        
    def depositar(self,valor):
        #self._saldo += valor
    
    def sacar(self,valor):
        #self._saldo -= valor
    
    def mostrarSaldo(self):
        return self._saldo
    
Conta = Conta("001",100)
Conta.depositar(100)
print(Conta.numeroAgencia)
print(Conta.mostrarSaldo())

#property()

print("\n")

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento


 = Pessoapessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
        
        
        
    
