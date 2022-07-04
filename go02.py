print('Bem vindo a Lanchonete do Lucas Moraes Da Silva RU:683164\n')

print('Aqui está o seu Cardápio...')

print("|Código|     |       Descrição       |       |   Valor  |")

print("| 100  |     |    Cachorro-Quente    |       |  R$9,00  |")

print("| 101  |     | Cachorro-Quente Duplo |       |  R$11,00 |")

print("| 102  |     |         X_Egg         |       |  R$12,00 |")

print("| 103  |     |        X-Salada       |       |  R$13,00 |")

print("| 104  |     |        X-Bacon        |       |  R$14,00 |")

print("| 105  |     |         X-Tudo        |       |  R$17,00 |")

print("| 200  |     |   Refrigerante Lata   |       |  R$5,00  |")

print("| 201  |     |      Chá Gelado       |       |  R$4,00  |")    

valorTotal=0

opcao683164=1

while(opcao683164==1):
    codigo = int(input('\nEntre com o código do produto desejado:'))  

    if codigo == 100:
        valorTotal += 9
        print('Você pediu um Cachorro-Quente no valor de R$9,00')

    elif codigo == 101:
        valorTotal += 11
        print('Você pediu um Cachorro-Quente Duplo no valor de R$11,00')

    elif codigo == 102:
        valorTotal += 12
        print('Você pediu um X-Egg no valor de R$12,00')

    elif codigo == 103:
        valorTotal += 13    
        print('Você pediu um X-Salada no valor de R$13,00')

    elif codigo == 104:
        valorTotal += 14
        print('Você pediu um X-Bacon no valor de R$14,00')

    elif codigo == 105:
        valorTotal+=17
        print('Você pediu um X-Tudo no valor de R$17,00')

    elif codigo == 200:
        valorTotal+=5
        print('Você pediu um Refrigerante Lata no valor de R$5,00')

    elif codigo == 201: 
        valorTotal += 4
        print('Você pediu um Chá Gelado no valor de R$4,00')

    else:
        print('Este código de produto não existe, digite uma opção válida') 
        continue

    opcao683164 = int(input('''Deseja fazer um novo pedido?\n1 - SIM\n0 - NÃO\n'''))
   
    print('O total a ser pago é:R$ {:.2f}'.format(valorTotal))          

    print('RU:683164\nlucas Moraes Da Silva')

print("Obrigad! voltem sempre!")