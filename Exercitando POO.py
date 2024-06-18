class Cliente:
    def __init__(self, nome: str, cpf: int):
        self._nome = nome
        self._cpf = cpf
    
    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf
    
    @staticmethod
    def cadastrar_cliente(nome: str, cpf: int, clientes: list):
        clientes.append([cpf, nome])
    
    @staticmethod
    def verificar_cliente(cpf: int, clientes: list):
        for cliente in clientes:
            if cpf == cliente[0]:
                return True
        return False

class Conta:
    def __init__(self, cliente):
        self._cliente = cliente
        self._saldo = 0
        self._extrato = []
    
    def depositar(self, valor):
        assert valor > 0, "Valor deve ser maior que zero"
        self._saldo += valor
        self._extrato.append(f'Depósito: R${valor:.2f}')
    
    def sacar(self, valor):
        assert valor > 0, "Valor deve ser maior que zero"
        assert self._saldo >= valor, "Saldo insuficiente"
        self._saldo -= valor
        self._extrato.append(f'Saque: R${valor:.2f}')
    
    def extrato(self):
        for item in self._extrato:
            print(item)
    
    @property
    def saldo(self):
        return self._saldo
    
    def __str__(self):
        return f'\nSaldo: R${self.saldo:.2f}'

class Interface:
    def __init__(self):
        self._cliente = None
        self._conta = None
        
        self.menu = '''
        --------- M E N U ---------
        Bem vindo ao Banco Ultramari!
        Você já tem uma conta?
        [s] = Sim   |  [n] = Não
        '''
        
        self.menu2 = '''
        -------- M E N U --------
        O que deseja fazer com sua conta?
        [d] = Depositar dinheiro na minha conta
        [s] = Sacar da minha conta
        [q] = Quit
        '''
    
    def login(self, clientes):
        resposta = input(self.menu).strip().lower()

        if resposta == "s":
            nome = input("Digite seu nome: ").strip()
            cpf = int(input("Digite seu CPF: ").strip())

            if Cliente.verificar_cliente(cpf, clientes):
                print("Bem vindo ao banco!")
                for cliente in clientes:
                    if cpf == cliente[0]:
                        self._cliente = Cliente(cliente[1], cliente[0])
                        self._conta = Conta(self._cliente)
                        break
            else:
                print("CPF não encontrado.")

        elif resposta == "n":
            cpf = int(input("Cadastre-se! Digite seu CPF: ").strip())
            nome = input("Agora digite seu nome: ").strip()
            Cliente.cadastrar_cliente(nome, cpf, clientes)
            self._cliente = Cliente(nome, cpf)
            self._conta = Conta(self._cliente)
            print("Cadastrado com sucesso. Bem vindo ao banco Ultramari!")

        else:
            print("Opção inexistente.")

    def operacoes(self):
        while True:
            operacao = input(self.menu2).strip().lower()
            
            if operacao == "d":
                valor = float(input("Digite o valor do depósito: R$"))
                self._conta.depositar(valor)
                print(f"Depósito de R${valor:.2f} realizado com sucesso.\n{self._conta}")
                
            
            elif operacao == "s":
                valor = float(input("Digite o valor do saque: R$"))
                self._conta.sacar(valor)
                print(f"Saque de R${valor:.2f} realizado com sucesso.\n{self._conta}")
                
            
            elif operacao == "q":
                break
            
            else:
                print("Opção inválida.")

def main():
    clientes = []
    interface = Interface()
    interface.login(clientes)
    interface.operacoes()

if __name__ == "__main__":
    main()
