#🎯 Desafio: Contagem de Consoantes
#Objetivo:
#Crie um programa que:
#Peça ao usuário para digitar uma frase.
#Armazene todas as consoantes dessa frase em uma lista.
#o final, o programa deve exibir:
#A lista de consoantes encontradas (você pode optar por armazená-las em letras minúsculas, por exemplo).
#O número de consoantes diferentes (usando set()).
#A quantidade de ocorrências de cada consoante na frase



frase = input("Digite uma frase: ")
consoantes = []

for palavras in frase: 
    if palavras.lower() in "bcdfghjklmnpqrstvxywez":
        consoantes.append(palavras)


print("\n📌 Sua frase foi:", frase)
print("🔡 Lista de consoantes encontradas:", consoantes)
print("🔢 Quantidade de consoantes diferentes:", len(set(consoantes)))

# Contando ocorrências de cada consoante encontrada
print("\n📊 Ocorrências de cada consoante:")
for c in sorted(set(consoantes)):
    print(f"Letra '{c}': {consoantes.count(c)}x")