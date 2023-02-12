'''
1 - cadastrar um usuario;
2 - verificar sua renda;
3 - verificar se esta com nome sujo ou limpo;
4 - Se estiver com nome sujo, encerrar o programa, senao, verificar renda mensal;
5 - se renda mensal > 3.500, liberar limite de 5 mil;
6 - se renda mensal >= 2.500 e < 3.500 , liberar limite de 2.000.
7 - se renda mensal >= 1.500 e < 2.500 , liberar com 50% de entrada;
8 - se renda < 1500 , não disponibiliza crediario.
9 - para cada limite um tipo de produto.

#fim
'''
def fim():
    print('-----------------------------------------')
    print("  CÓDIGO TODO DIA AGRADECE A PREFERÊNCIA  ")
    print("          V O L T E   S E M P R E          ")
    print('-----------------------------------------')

#inicio
def boas_vindas():
    print('--------------------------------------')
    print('CÓDIGO TODO DIA APROVAÇÃO DE CREDIARIO')
    print('--------------------------------------''\n')


boas_vindas()

nome =  str(input("Digite seu Nome: "))
nome = nome.upper()
renda = int(input("Informe sua Renda Mensal: "))
opcao = int(input("DIGITE [1] NOME LIMPO , [2] NOME SUJO , [3] SAIR : "))

#MINHAS VARIAVEIS DE PRODUTOS, E VALORES DE RESPECTIVOS PRODUTOS
'''
produto1 = str("geladeira")
valor_produto1 = 3000
produto2 = str("televisao")
valor_produto2 = 3800
produto3 = str("sofá")
valor_produto3 = 4500
produto4 = str("fogão")
valor_produto4 = 1200
produto5 = str("armário")
valor_produto5 = 1600
produto6 = str("cama boxe")
valor_produto6 = 1800
produto6 = str("berço")
valor_produto6 = 600
produto6 = str("sanduicheira")
valor_produto6 = 300
produto6 = str("ayer fryer")
valor_produto6 = 700
'''

# INDEX PRODUTOS:  0          1         2        3         4          5         6            7               8               9            10          11

produtos = ("GELADEIRA", "TELEVISÃO", "SOFÁ", "FOGÃO", "ARMÁRIO", "CAMA-BOXE", "BERÇO", "SANDUICHEIRA", "AYER FRYER", "CAMERA DIGITAL","FRIGOBAR", "cÔMODA")

# INDEX valoresP :  0     1     2     3     4     5     6    7     8    9   10    11

valoresProdutos = (3000, 3800, 4500, 1200, 1600, 1800, 600, 300 , 700, 650, 530, 499)



while opcao != 3:
    if renda >= 3500 and opcao == 1 :
        print("Crediario Aprovado com Limite de até 5MIL!""\n")
    elif renda >= 2500 and renda <3500 and opcao == 1:
        print("Crediario Aprovado com Limite de até 2MIL""\n")
    elif renda >= 1200 and renda <2500 and opcao ==1:
        print("Crediario Aprovado, com 25% de entrada""\n")
    elif renda < 1200 and opcao == 1:
        print("NÃO TEMOS LIMITE DE CRÉDITO APROVADO PARA VOCE""\n")
    elif renda >100 and opcao == 2:
        print("VOCE ESTA COM O NOME SUJO, DESCULPE, NAO PODEMOS APROVAR SEU CREDIARIO.")
    break
while renda > 3500 and opcao == 1:
    escolha = int(input("QUAL PRODUTO DESEJA OBTER? : [4]GELADEIRA, [5] TELEVISÃO, [6] SOFÁ , [7] CANCELAR COMPRA: "))
    while escolha != 7:
        if escolha == 4:
            print("\n"f'VOCE ESCOLHEU O SEGUINTE PRODUTO : {str(produtos[0])}')
            print(f'O valor do produto é de R$: {(valoresProdutos[0])} reais')
            quantidade_parcelas = input("\n""DESEJA PARCELAR EM QUANTAS VEZES? ")
            parcelamento = int(valoresProdutos[0]) / int(quantidade_parcelas)
            print (f'O Produto {(produtos[0])} parcelado ficou em {quantidade_parcelas} x de R${parcelamento} sem juros.'"\n")
        elif escolha == 5:
            print("\n"f'VOCÊ ESCOLHEU O SEGUINTE PRODUTO : {str(produtos[1])}')
            print(f'O valor do produto escolhido avista é de R$: {str(valoresProdutos[1])} reais')
            quantidade_parcelas = input("DESEJA PARCELAR EM QUANTAS VEZES? ")
            parcelamento = int(valoresProdutos[1]) / int(quantidade_parcelas)
            print (f'O Produto {(produtos[1])} parcelado ficou em {quantidade_parcelas} x de R${parcelamento} sem juros.'"\n")
        elif escolha == 6:
            print("\n"f' VOCÊ ESCOLHEU O SEGUINTE PRODUTO : {str(produtos[2])}')
            print (f'O valor do produto é de R$: {str(valoresProdutos[2])} reais')
            quantidade_parcelas = input("DESEJA PARCELAR EM QUANTAS VEZES? ")
            parcelamento = int(valoresProdutos[2]) / int(quantidade_parcelas)
            print (f'O Produto {(produtos[2])} parcelado ficou em {quantidade_parcelas} x de R${parcelamento} sem juros.'"\n")
        break
    fim()
    break
while renda >= 2500 and renda <3500 and opcao == 1:
    escolha = int(input("QUAL PRODUTO DESEJA OBTER? : [4]FOGAO, [5] ARMARIO, [6] CAMA BOXE , [7] CANCELAR COMPRA: "))
    while escolha != 7:
        if escolha == 4:
            print("\n"f'VOCÊ ESCOLHEU O SEGUINTE PRODUTO : {str(produtos[3])}')
            print(f'O valor do produto é de R$: {valoresProdutos[3]} reais')
            quantidade_parcelas = input("\n""DESEJA PARCELAR EM QUANTAS VEZES? ")
            parcelamento = int(valoresProdutos[3]) / int(quantidade_parcelas)
            print(f'O Produto {produtos[3]} parcelado ficou em {quantidade_parcelas} x de R${parcelamento} sem juros.'"\n")
        elif escolha == 5:
            print("\n"f'VOCÊ ESCOLHEU O SEGUINTE PRODUTO : {str(produtos[4])}')
            print(f'O valor do produto escolhido avista é de R$: {str(valoresProdutos[4])} reais')
            quantidade_parcelas = input("DESEJA PARCELAR EM QUANTAS VEZES? ")
            parcelamento = int(valoresProdutos[4]) / int(quantidade_parcelas)
            print(f'O Produto {produtos[4]} parcelado ficou em {quantidade_parcelas} x de R${parcelamento} sem juros.'"\n")
        elif escolha == 6:
            print("\n"f'VOCÊ ESCOLHEU O SEGUINTE PRODUTO : {str(produtos[5])}')
            print(f'O valor do produto é de R$: {str(valoresProdutos[5])} reais')
            quantidade_parcelas = input("DESEJA PARCELAR EM QUANTAS VEZES? ")
            parcelamento = int(valoresProdutos[5]) / int(quantidade_parcelas)
            print(f'O Produto {produtos[5]} parcelado ficou em {quantidade_parcelas} x de R${parcelamento} sem juros.'"\n")
        break
    fim()
    break

def calculos():
    produtos1 = ("CAMERA DIGITAL", "FRIGOBAR", "COMODA")
    valores = (650, 550, 450)
    while renda >= 1200 and renda < 2500 and opcao == 1:
        escolha = int(input("QUAL PRODUTO DESEJA: [4]CAMERA DIGITAL, [5]FRIGOBAR, [6]CÔMODA, [7]CANCELAR :"))
        while escolha != 7:
            if escolha == 4:
                print("\n"f'VOCÊ ESCOLHEU O SEGUINTE PRODUTO : {str(produtos1[0])}')
                print(f'O valor do produto é de R$: {valores[0]} reais, com entrada no valor de 25%')
                entrada = valores[0] / 4
                print(f'O valor da entrada é de : R$ {entrada} ')
                restante = (valores[0] / 4) * 3
                print(f'O restante do valor a ser parcelado é de: R$ {restante}')
                quantidade_parcelas1 = int(input("DESEJA PARCELAR O RESTANTE EM QUANTAS VEZES? "))
                parcelamento = int(restante) / int(quantidade_parcelas1)
                print(f'SUA ENTRADA É NO VALOR DE R$: {entrada}')
                print(f'O Produto {produtos1[0]} com entrada de R${entrada} fica o restante de {quantidade_parcelas1} parcelas de R${parcelamento} sem juros.'"\n")
            elif escolha == 5:
                print("\n"f'VOCÊ ESCOLHEU O SEGUINTE PRODUTO : {str(produtos1[1])}')
                print(f'O valor do produto é de R$: {valores[1]} reais, com entrada no valor de 25%')
                entrada = valores[1] / 4
                print(f'O valor da entrada é de : R$ {entrada} ')
                restante = (valores[1] / 4) * 3
                print(f'O restante do valor a ser parcelado é de: R$ {restante}')
                quantidade_parcelas1 = int(input("DESEJA PARCELAR O RESTANTE EM QUANTAS VEZES? "))
                parcelamento = int(restante) / int(quantidade_parcelas1)
                print(f'SUA ENTRADA É NO VALOR DE R$: {entrada}')
                print(f'O Produto {produtos1[1]} com entrada de R${entrada} fica o restante de {quantidade_parcelas1} parcelas de R${parcelamento} sem juros.'"\n")
            elif escolha == 6:
                print("\n"f'VOCÊ ESCOLHEU O SEGUINTE PRODUTO : {str(produtos1[2])}')
                print(f'O valor do produto é de R$: {valores[2]} reais, com entrada no valor de 25%')
                entrada = valores[2] / 4
                print(f'O valor da entrada é de : R$ {entrada} ')
                restante = (valores[2] / 4) * 3
                print(f'O restante do valor a ser parcelado é de: R$ {restante}')
                quantidade_parcelas1 = int(input("DESEJA PARCELAR O RESTANTE EM QUANTAS VEZES? "))
                parcelamento = int(restante) / int(quantidade_parcelas1)
                print(f'SUA ENTRADA É NO VALOR DE R$: {entrada}')
                print(f'O Produto {produtos1[2]} com entrada de R${entrada} fica o restante de {quantidade_parcelas1} parcelas de R${parcelamento} sem juros.'"\n")
            break
        fim()
        break

calculos()

