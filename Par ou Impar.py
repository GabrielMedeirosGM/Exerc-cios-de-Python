pares =[]
impares =[]
numeros =[]
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

    # Verifica se é par ou ímpar e adiciona na lista correta
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(" Lista completa:", numeros)
print(" Números pares:", pares)
print(" Números ímpares:", impares)