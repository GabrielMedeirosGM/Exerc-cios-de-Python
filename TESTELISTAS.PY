num = [] #lista original

for x in range(4):
    numero = float(input(f"digite o {x+1}º número: "))
    num.append(numero)

modify = num[:] #faz cópia da lista original, agora posso atribuir variaveis para modificar a lista sem alterar a original
modify.insert(2, 15.00) 

print("foi isso que voce escreveu",num)
print(f"com Sort: {sorted(num, reverse=True)}") # sorted = nova lista ordenada sem alterar a original sort= quando quiser ordenar que ja venha assim alterando a lista.
print(f'Essa lista tem {len(num)} elementos') #len faz a contagem de elementos no index da lista
print("Apenas com o insert",modify) #tabela original apenas com o valor inserido (se eu quisesse juntar insert sort com modify, ele me apresentaria os valores com insert e organizados.) 

# Pedir ao usuário para escolher o índice do item a ser removido|| len(modify)-1 = como o indice tem 5 elementos
indice = int(input(f"Digite o indíce que deseja remover de 0 a {len(modify)-1}):"))

if 0 <= indice < len(modify):
    removido = modify.pop(indice)  # remove e retorna o item no índice escolhido
    print(f"Número {removido} foi removido.")
else:
    print("Índice inválido!")

# Exibir a lista após a remoção
print("Lista após a remoção:", modify)