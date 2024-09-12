# Dia 6 - 09/09/2024
# Faça um programa que calcula o fatorial de um número. (Python)

numero = int(input("Fatorial de: ") )

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)