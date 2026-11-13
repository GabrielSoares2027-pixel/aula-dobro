
nome = input("Nome do cachorro: ")
idade = int(input("Idade do cachorro: "))
porte = int(input("Porte (1-Grande, 2-Médio, 3-Pequeno): "))
banhos = int(input("Quantidade de banhos em 12 meses: "))

idade_cachorro = idade + idade + idade + idade + idade + idade + idade

lucros = [55, 45, 45]
lucro_banho = lucros[porte - 1]
lucro_anual = lucro_banho * banhos

print("Olá,", nome, "tem", idade_cachorro, "anos e nos últimos 12 meses o lucro com este animal foi de R$", lucro_anual)
