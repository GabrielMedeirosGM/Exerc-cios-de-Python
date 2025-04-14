#Crie um programa que:
#Peça ao usuário para digitar uma frase.
#Armazene as vogais dessa frase em uma lista.
#No final, o programa deve exibir:
#A lista de vogais que aparecem na frase.
#O número de vogais diferentes.
#O número de ocorrências de cada vogal na frase.

frase = input("Digite uma frase")
vogais = []

for letra in frase:
    # Verifica se o caractere é uma vogal (minúscula ou maiúscula)
    if letra.lower() in 'aeiou':
        vogais.append(letra)

# Exibindo os resultados
print("Vogais encontradas:", vogais)
print("Número de vogais diferentes:", len(set(vogais)))  # Conjunto de vogais únicas

# Contagem das ocorrências de cada vogal
for vogal in 'aeiou':
    print(f"Ocorrências de '{vogal}': {vogais.count(vogal)}")