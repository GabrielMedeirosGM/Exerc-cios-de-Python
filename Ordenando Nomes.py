nomes = []
for x in range(5):
    nome = str(input(f"Digite o {x+1}º nome: "))
    nomes.append(nome)

# Exibe a lista original após o loop
print("Nos escrevemos:", nomes)

# Exibe a lista em ordem alfabética
print("Em ordem alfabética ficou:", sorted(nomes))

# Inverte a lista original
nomes.reverse()
print("Em ordem reversa ficou:", nomes)