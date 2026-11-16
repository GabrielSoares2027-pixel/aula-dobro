# 1. Criar tupla com 5 dados
tupla = ("Maçã", "Banana", "Uva", "Pera", "Laranja")

# 2. Converter para lista
lista = list(tupla)

# 3. Inserir 2 dados extras
lista.append("Manga")
lista.append("Abacaxi")

# 4. Remover o primeiro
lista.pop(0)

# 5. Remover o último
lista.pop()

# 6. Print do primeiro dado
print(lista[0])

# 7. Print da quantidade de dados
print(len(lista))

# 8. Criar o dicionário
pessoa = {
    "Nome": "Ana",
    "Idade": 25,
    "Profissão": "Programadora"
}

# 9. Imprimir apenas o valor da chave Nome
print(pessoa["Nome"])