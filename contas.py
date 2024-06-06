class Conta():
    """
    Classe conta
    """
    _saldo = 0.0

    def __init__(self, numero, titular, senha, saldoi= 0.0):
        """
        Construtor da classe Conta

        parametro numero é o numero do titular da conta
        parametro titular é o nome do titular da conta
        parametro senha é a senha usada para acessar a conta
        parametro saldoi é o valor inicial que se o cliente não infomar será 0

        """
        self.numero= numero
        self.titular= titular
        self.__senha= senha
        self._saldo= saldoi

    def getsaldo(self,senha):
        if self.__senha == senha:
            return self._saldo
    def setsaldo(self,valor):
        self._saldo = valor
    def setsenha(self,novasenha):
        self.__senha = novasenha
    def saque(self,senha,valor):
        if senha == self.__senha:
            if valor <= self._saldo:
                self._saldo -= valor
                print(f"Saque no valor de: RS{valor} foito com sucesso")
            else:
                print("valor invalido")
        else:
            print("senha invalida")
    def deposito(self,valor):
        if valor > 0:
            self._saldo += valor
            print("deposito feito com sucesso")
        else:
            print("valor invalido")
    def exibedados(self,senha):
        if senha == self.__senha:
            print(self.numero,self.titular,self._saldo)
        else:
            print("senha invalida")
            
    def exibedados2(self):
        print(self.numero,self.titular,self._saldo)
       
        


class contapupanca(Conta):
    """
    Classe conta poupança 

    """
    def __init__(self, numero, titular, senha,taxa = 0.02, saldoi = 0.0):
        super().__init__(numero,titular,senha,saldoi)
        self.__taxa= taxa
    def simularendimeento(self,nmeses):
        if nmeses> 0:
           saldoFinal = self._saldo*pow((1+self.__taxa),nmeses)
           print(f"Saldo após {nmeses} é R$: {saldoFinal}")
        else:
            print("Numnero de meses deve ser maior que 0")

class Banco:
    

    def __init__(self,senha):
        self.__senha = senha

         
        
    def criarConta(self, Conta):
        self.lista.append= [Conta]

    def excluirConta(self, Conta):
        self.lista.pop= [Conta]

    def setsenha(self, Novasenha,senhaAntiga):
       if senhaAntiga == self.__senha:

         self.__senha = Novasenha
         print("senha trocada com sucesso")
         
        
