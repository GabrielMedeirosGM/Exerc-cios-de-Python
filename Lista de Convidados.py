#Objetivo:
#Crie um programa que:
#Peça ao usuário para digitar o nome de 5 convidados e armazene numa lista.
#Depois, pergunte o nome de 1 pessoa e verifique:
#Se essa pessoa está na lista de convidados, diga: "Entrada permitida!"
#Se não estiver, diga: "Você não está na lista!"

convidados = []

for i in range(2):
    nome = input(f"Digite o {i+1}º nome : ")
    convidados.append(nome)

print(convidados) 

verificador = input("Digite o nome para verificar: ")

if verificador in convidados:
    print("nome na lista, pode entrar!")
else:
    print("seu nome nao está na lista")