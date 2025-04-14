#Solicite ao usuário que insira 5 idades (como números inteiros).

#Calcule a média das idades.

#Determine a mais nova (mínima) e a mais velha (máxima) idade.

#Conte quantas pessoas têm mais de 18 anos.


idades = []
nomes = []

for x in range(3):
    idade = float(input("Digite sua idade: "))
    nome = str(input("Digite seu nome: "))

    idades.append(idade)
    nomes.append(nomes)

media = sum(idades) / len(idades)
min = min(idades) 
max= max(idades)

print("a media de idade é", media)
print("a menor idade é ", min)
print("a maior idade é ", max)