def menu():
    print(""" ******Bem-vindo ao Sistema do Banco! Por favor escolha uma das opções abaixo: ******
[1]Sacar
[2]Depositar
[3]Extrato
[0]Sair""")
    
    while True:
        global saldo, operacoes, tentativas
        
        user = input("\nOpção: ")
        if user == "1":
            tentativas += 1
            return sacar()
        elif user == "2":
            return depositar()
        elif user == "3":
            return extrato()
        elif user == "0":
            print("Obrigado por utilizar nosso sistema!! ")
            break
        else: 
            print("Opção inválida!! Tente novamente. \n")
            return menu()
     
def sacar():
    global saldo, operacoes
    max_tentativas = 3   

    while tentativas <= max_tentativas:
        valor_saque = int(input("Digite o valor desejado: \n"))
                
        if valor_saque <= 0:
            print("Operação inválida! \n")
            return menu()

        elif saldo < valor_saque:
            print("Sem saldo em conta! Operação finalizada. \n")
            return menu()
        elif valor_saque > 500:
            print("Limite por saque de R$ 500 atingido! Por favor tente outro valor. \n")
        else:
            saldo = saldo - valor_saque
            operacoes.append({"Tipo: ": "Saque ", "valor: R$ ": valor_saque})
            print(f"Saque realizado com sucesso!! Seu novo saldo é de R${saldo}. \n")
            return menu()
    print("Limite de saques diários atingido. Por favor tente novamente amanhã, obrigado!! \n")
    return menu()
        
def depositar():
   global saldo, operacoes
   valor_deposito = int(input("Digite o valor desejado: \n"))

   if valor_deposito <= 0:
        print("Operação inválida! \n")
        return menu()

   else:
        saldo = saldo + valor_deposito
        operacoes.append({"Tipo: ": "Deposito ","Valor: R$ ":valor_deposito})
        print(f"Deposito realizado com sucesso!! Seu novo saldo é de R${saldo}. \n")
        return menu()

def extrato():
    global saldo, operacoes
    print("****************** EXTRATO ****************** \n")
    print("Aqui estão suas últimas operações realizada: \n")
    print(f"Seu saldo atual é de R$ {saldo}.\n")
    if operacoes == []:
            print("Não foram realizadas operações! \n")
            return menu()
    for i in operacoes:
        print(f"Operação  {i}\n")
    
    return

    






operacoes = []
tentativas = 0
saldo = 1000
menu()