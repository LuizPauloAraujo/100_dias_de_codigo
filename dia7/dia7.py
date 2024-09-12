# Dia 7 - 10/09/2024
# Escreva um programa que calcula a tabuada de um número. (Python)

tabuada=int(input("Tabuada do numero: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )