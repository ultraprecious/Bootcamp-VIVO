#Sistema Bancário
deposito = 0
saque = 0
extrato = ''

def depositar() :
  controle = True

  while controle:
    valor = float(input("Informe o valor do depósito:"))

    if type(valor) != float or int:
      print('Entrada inválida para a operação. Digite uma entrada válida.')


    else:
      controle = False
      deposito = valor + deposito
      print("Depósito de {valor} realizado!")
      

def saque():
  valor = float(input("Informe o valor do saque: "))
  controle = True
  
  while controle:
    if valor > 500:
      print("Não são permitidos saques a partir de R$500.00.\n Saque um valor inferior")
      

    else:
      print(f'Saque de R${valor:.2f} realizado!')

  



menu = f'''
***** MENU *****
Digite a letra entre os colchetes para escolher a operação desejada:
[d] = depositar

[s] = saque

[e] = extrato

[q] = sair
'''

controle = True

while controle:
  letra = str(input())

  if letra == "d" :
    depositar()

  if letra == "s" :
    saque()

  if letra == "e" :
    extrato()

  if letra == "q" :
    print("Saindo do sistema...")
    controle = False
  
  else:
    print("Operação inválida. Digite as opções válidas do MENU.")