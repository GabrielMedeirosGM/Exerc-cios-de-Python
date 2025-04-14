lista= []

for x in range(5):
    produtos = str(input("Digite os produtos no carrinho : "))
    lista.append(produtos)
    print(lista)

remover = input("Digite o intem da lista que queira remover")

if remover in lista:
    lista.remove(remover)
    print(f"{remover} foi removido com sucesso!")
else:
    print("o item nao está na lista")

print("assim ficou a lista" , lista)
print("quantidade de itens da lista", len(lista))

if lista == 0:
    print("A lista está vazia")
else:
    print("a lista ainda possui itens")