class Usuario:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    def hacer_deposito(self,amount):
        self.balance_cuenta+=amount
        return self
    def hacer_retiro(self,amount):
        self.balance_cuenta-=amount
        return self
    def mostrar_balance_usuario(self):
        print("User: %s, Balance: %d"%(self.name,self.balance_cuenta))
    def transferir_dinero(self, other_user,amount):
        self.hacer_retiro(amount)
        other_user.hacer_deposito(amount)
        return self

diego = Usuario("Diego","diego@example.com")
diego.hacer_deposito(1200).hacer_deposito(1550).hacer_deposito(1400).hacer_retiro(1350).mostrar_balance_usuario()

gabriel = Usuario("Gabriel","gabriel@example.com")
gabriel.hacer_deposito(1350).hacer_deposito(1350).hacer_retiro(400).hacer_retiro(800).mostrar_balance_usuario()

marco = Usuario("Marco","marco@example.com")
marco.hacer_deposito(200).hacer_retiro(250).hacer_retiro(250).hacer_retiro(250).mostrar_balance_usuario()

diego.transferir_dinero(marco,800)

print("-------- Después de transferir dinero --------")
diego.mostrar_balance_usuario()
marco.mostrar_balance_usuario()
