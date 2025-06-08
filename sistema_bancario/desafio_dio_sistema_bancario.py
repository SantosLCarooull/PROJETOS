from datetime import date, datetime
def menu():
    print(""" ******Bem-vindo ao Sistema do Banco! Por favor escolha uma das opções abaixo: ******
[1]Sacar
[2]Depositar
[3]Extrato
[0]Sair""")
    
    while True:
        global saldo, operacoes, transacoes
        
        user = input("\nOpção: ")
        if user == "1":
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
    global saldo, operacoes, transacoes, transacoes_diarias
    
    while transacoes < transacoes_diarias:
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
            operacoes.append({"Tipo: ": "Saque ", "valor: R$ ": valor_saque, "Data: ":horario.strftime(horario_ptbr)})
            print(f"Saque realizado com sucesso!! Seu novo saldo é de R${saldo}. \n")
            transacoes +=1
            return menu()
    print("Limite de transações diárias atingido. Por favor tente novamente amanhã, obrigado! ")
    return menu()
        
def depositar():
    global saldo, operacoes, transacoes, transacoes_diarias
      
    while transacoes < transacoes_diarias:
        valor_deposito = int(input("Digite o valor desejado: \n"))
        if valor_deposito <= 0:
            print("Operação inválida! \n")
            return menu()

        else:
            saldo = saldo + valor_deposito
            operacoes.append({"Tipo: ": "Deposito ","Valor: R$ ":valor_deposito,"Data: ":horario.strftime(horario_ptbr)})
            print(f"Deposito realizado com sucesso!! Seu novo saldo é de R${saldo}. \n")
            transacoes +=1
            return menu()
       
    print("Limite de transações diárias atingido. Por favor tente novamente amanhã, obrigado! ")
    return menu()

def extrato():
    
    print("******************************************** EXTRATO *********************************************\n")
    print("Aqui estão suas últimas operações realizada: \n")
    print(f"Seu saldo atual é de R$ {saldo}.\n")
    if operacoes == []:
            print("Não foram realizadas operações! \n")
            return menu()
    for i in operacoes:
        print(f"Operação  {i}\n")
        
    print("***************************************************************************************************\n")
    
    return menu()




horario = datetime.now()
horario_ptbr ="%d/%m/%Y %H:%M"
operacoes = []
transacoes = 0
transacoes_diarias = 10
saldo = 1000

menu()