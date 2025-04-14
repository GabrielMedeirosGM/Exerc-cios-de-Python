######################Analisador de Notas

# Criando uma lista vazia para armazenar as notas
notas = []

# Criando uma lista vazia para armazenar os nomes dos alunos
nomes = []

# Loop para solicitar os dados de 4 alunos
for x in range(4):
    # Solicitando o nome do aluno
    nome = input("Digite seu nome: ")
    
    # Solicitando a nota do aluno, convertendo o valor para float (número decimal)
    nota = float(input("Digite a nota: "))

    # Adicionando o nome do aluno na lista de nomes
    nomes.append(nome)
    
    # Adicionando a nota do aluno na lista de notas
    notas.append(nota)

# Calculando a média das notas (soma de todas as notas dividida pelo número de notas)
media = sum(notas) / len(notas)

# Encontrando a maior nota da lista
maior = max(notas)

# Encontrando a menor nota da lista
menor = min(notas)

# Pegando o índice da maior nota na lista para associar ao nome do aluno
indice_maior = notas.index(maior)

# Pegando o índice da menor nota na lista para associar ao nome do aluno
indice_menor = notas.index(menor)

# Exibindo os resultados
print("\nResultados:")
# Exibindo a lista de todas as notas
print("Notas:", notas)

# Exibindo a lista de todos os nomes
print("Nomes:", nomes)

# Exibindo a média das notas, formatada com 2 casas decimais
print(f"Média final: {media:.2f}")

# Exibindo quem tirou a maior nota, com o nome do aluno e a nota
print(f"Maior nota: {maior} - {nomes[indice_maior]}")

# Exibindo quem tirou a menor nota, com o nome do aluno e a nota
print(f"Menor nota: {menor} - {nomes[indice_menor]}")
