from contas import Conta, contapupanca, Banco

print("Bem vindo ao sistema bancário de atendimento online")
lista = []
while True:
    a = int(input("digete seu perfil: (1)- cliente  //  (2)- funcionario   //   (3)- sair "))

    if a == 2:
        a = int(input("1- mudança da senha do gerente // 2- cadastro de novos cliente  // 3- ver clientes cadastrados  // 4- encerrar ultimo cadastro feito "))
        gerente = Banco(1234)
        if a == 1:
            novaSenha = int(input("digite a nova senha"))
            velhaSenha = int(input("digite a senha antiga"))
            gerente.setsenha(novaSenha,velhaSenha)
        elif a == 2:
            print(" para o cadastro de novos clientes ensira as seguintes informações ")
            Numero = int(input("Numero da conta "))
            Titulo = input("Nome do usuario ")
            Senhai = int(input("Senha inicial "))
            SaldoInicial = float(input("Saldo inicial "))
            c1 = Conta(Numero, Titulo, Senhai, saldoi = SaldoInicial)
            lista.append(c1) 
            
            
            
        elif a == 3:
            for c1 in lista:
                print(c1.exibedados2())
        elif a == 4:
            
            lista.pop()
                
            
        else:
            print("operação invalida")
    

    elif a == 1:
        a = int(input("qual ação deseja fazer: (1)- deposito  //  (2)- saque   //  (3)- ver saldo "))
        if a == 1:
            valor2 = float(input("digete o valor que deseja depositar: R$"))
            c1.deposito(valor2)

        elif a == 2:
            valor1 = float(input("digete o valor que deseja sacar: R$"))
            c1.saque(Senhai,valor1)
        elif a == 3:
            c1.exibedados(Senhai)
        else:
            print("operação invalida")




    elif a == 3:
            break
        
    
        

        
            



