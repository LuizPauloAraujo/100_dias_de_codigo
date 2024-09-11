def adicao(x, y):
  return x + y

def subtracao(x, y):
  return x - y

def multiplicacao(x, y):
  return x * y

def divisao(x, y):
  return x / y

def calculadora():
  print("Selecione a operação")
  print("1. Adição")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")


  while True:
    escolha = input("Escolha uma opção (1/2/3/4): ")
    if escolha in ('1', '2', '3', '4'):
      x = float(input("Digite o primeiro número: "))
      y = float(input("Digite o segundo número: "))
      if escolha == '1':
        print("Resultado:", adicao(x, y))
      if escolha == '2':
        print("Resultado: ", subtracao(x, y))
      if escolha == '3':
        print("Resultado: ", multiplicacao(x, y))
      if escolha == '4':
        if y != "0":
          print("Resultado: ", divisao(x, y))
      else:
        print("Não é possível dividir por zero")
    else:
      print("Escolha inválida")
      Continuar = input("Deseja continuar? (s/n): ")
      if Continuar == "n":
        print("Calculadora encerrada")
        break
      
  calculadora()
