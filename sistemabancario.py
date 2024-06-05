#Sistema Bancário
def depositar() :
  global conta
  controle = True

  while controle:
    valor = float(input("Informe o valor do depósito:"))

    if type(valor) != float:
      msg = input(f'''
            Entrada inválida para a operação. Digite uma entrada válida.
            Para voltar ao MENU, digite "q".
            Para continuar e inserir o valor de depósito, dê ENTER. ''')
      if msg == "q":
        controle = False


    else:
      controle = False
      conta = valor + conta
      print(f'Depósito de R${valor:.2f} realizado!')
      historico.append(f'Depósito: R${valor:.2f}')

      print(f'Saldo atual:R${conta:.2f}')
      

def sacar():
  global conta
  
  controle = True
  
  while controle:
    valor = float(input("Informe o valor do saque: "))

    if valor > 500:
      print("Não são permitidos saques a partir de R$500.00.\nSaque um valor inferior")
  

    elif valor < 0:
      print("Valor inválido inserido. Digite outro valor") 
    
    elif type(valor) != float:
      msg = input(f'''Entrada inválida para a operação. Digite uma entrada válida.
            Para voltar ao MENU, digite "q".
            Para continuar e inserir o valor de depósito, dê ENTER. ''')

      if msg == "q":
        controle = False
    
    elif valor > conta:
      print(f'Valor maior que o encontrado na conta (R${conta:.2f}). Operação invalidada, tente novamente.')


    else:
      controle = False
      print(f'Saque de R${valor:.2f} realizado!')
      conta = conta - valor
      historico.append(f'Saque: R${valor:.2f}')

      print(f'Saldo atual:R${conta:.2f}')

def extrato(historico):
  global conta
  auxiliar = 1
  for i in historico:
    print(f'{auxiliar} - {i}')
    auxiliar += 1

  print(f'Saldo atual:R${conta:.2f}')

conta = 0
saque = 0
historico = []

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
  letra = str(input(menu))

  if letra == "d" :
    depositar()

  elif letra == "s" :
    sacar()

  elif letra == "e" :
    extrato(historico)

  elif letra == "q" :
    print("Saindo do sistema...")
    controle = False
  
  else:
    print("Operação inválida. Digite as opções válidas do MENU.")