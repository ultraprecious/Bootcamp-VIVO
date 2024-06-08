from datetime import date

def criar_usuario(nome,data,cpf,endereco,usuarios):
    
    cpf_formatado =  cpf.replace(".","").replace("-","")
    usuario       =  {'Nome': nome ,'Data':data,  'CPF':cpf_formatado  ,  'Endereço':endereco} 

    for i in range(len(usuarios)):
        if cpf_formatado != usuarios[i]['CPF']:
            usuarios.append(usuario)
        else:
            print(f'Usuário com CPF já cadastrado.')

def criar_conta(usuario, cpf):
    global contas, usuarios
    usuario_existente = False
    
    for user in usuarios:
        if cpf == user["CPF"] and usuario == user['Nome']:
            usuario_existente = True
            break
    
    if usuario_existente:
        conta = {'Agência': '0001', 'Nº conta': len(contas) + 1, 'Usuário': usuario}
        contas.append(conta)
        print("Conta criada!")
    else:
        print("Usuário não cadastrado. Para criar uma conta, cadastre seu usuário.")


def sacar(*,valor,limite,extrato,numero_saques,limite_saques): 
    global saldo
    if numero_saques > limite_saques   or   valor > limite   or   valor > saldo:
        if numero_saques > limite_saques:
            print(f"Operação inválida: Limite de saques diários excedidos. Tente outro dia.")
        
        elif valor > limite:
            print(f'Operação inválida: Não é permitido sacar mais de R${limite:.2f}.')
        
        elif valor > saldo:
            print(f'Operação inválida: Saque maior que o saldo da conta (R${saldo:.2f}.)')
    
    else:
        print(f'Saque de {valor} realizado.\nSaldo atual:R${(saldo-valor):.2f}')
        extrato.append(f'{len(extrato)+1}. Saque:R${valor:.2f}')
        numero_saques += 1
    
def depositar(valor,extrato):
    global saldo
    if valor > 0:
        print(f'Depósito de R${valor:.2f} realizado.\nSaldo atual:R${(saldo+valor):.2f}')
        saldo = saldo + valor
        extrato.append(f'{len(extrato)+1}. Depósito:R${valor:.2F}')
    else:
         print("Valor de depósito inválido.")

def f_extrato(extrato):
    a = 1
    for i in extrato:
        print(f'{a}. {i}')
        a += 1



menu = f'''
***** MENU *****
Digite a letra entre os colchetes para escolher a operação desejada:
[u] = Novo usuário

[c] = Nova conta

[d] = Depositar

[s] = Saque

[e] = Extrato

[q] = Sair
'''


usuarios = list()
contas = list()
extrato = list()
saldo = 0
limite_saques = 3
numero_saques = 0
limite = 500
controle = True

while controle:
    letra = str(input(menu))

    if letra == "d" :
        valor = float(input("Digite o valor do depósito:\nR$"))
        depositar(valor,extrato)

    elif letra == "s" :
        valor = float(input("Digite o valor do saque:\nR$"))
        sacar(valor = valor,limite = limite,extrato = extrato,numero_saques = numero_saques ,limite_saques = limite_saques)

    elif letra == "e" :
        f_extrato(extrato)
        print(extrato)

    elif letra == "q" :
        print("Saindo do sistema...")
        controle = False

    elif letra == "u":
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF (sem pontos e traços se possível): ")
        endereco = input("Informe seu CEP: ")
        data = date.today()
        criar_usuario(nome,data,cpf,endereco,usuarios)

    elif letra == 'c':
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF (sem pontos e traços se possível): ")
        criar_conta(nome,cpf)

    else:
        print("Operação inválida. Digite as opções válidas do MENU.")



