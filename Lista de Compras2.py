#🎯 Desafio: Carrinho de Compras
#Objetivo:

#Crie um programa que armazene o nome de 5 produtos e o preço de cada produto em listas separadas.

#No final, o programa deve:

#Exibir os produtos e seus respectivos preços.

#Calcular o valor total da compra.

#Exibir o produto mais caro e o produto mais barato.

nome_produto= []
preco_produto = []

for x in range(2):
    nome = input(f"Digite o {x+1}º nome do item: ")
    preco = float(input("Digite o valor do item: "))
    nome_produto.append(nome)
    preco_produto.append(preco)
  
    
total = sum(preco_produto)
produto_caro = max(preco_produto)
produto_barato = min(preco_produto)
indice_caro = preco_produto.index(produto_caro)
indice_barato = preco_produto.index(produto_barato)

print(f"\n💰 Total da compra: R$ {total:.2f}")
print(f"🔝 Produto mais caro: {nome_produto[indice_caro]} - R$ {produto_caro:.2f}")
print(f"🔻 Produto mais barato: {nome_produto[indice_barato]} - R$ {produto_barato:.2f}")