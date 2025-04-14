#🎯 Desafio: Encontrar o Maior e Menor Número
#Objetivo:

#Crie um programa que:

#Peça ao usuário para digitar 10 números inteiros e os armazene em uma lista.

#Depois, o programa deve:

#Exibir a lista de números.

#Calcular e exibir o maior número e o menor número da lista.


numeros = []
for x in range(5):
    numero = int(input(f"Digite {x+1}º Número:  "))
    numeros.append(numero)


print(numeros)

max = max(numeros)
total = sum(numeros)
min = min(numeros)

print(max)
print(total)
print(min) 