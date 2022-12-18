class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance = 0 ):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Hola {self.nombre} {self.apellido}\nNumero de cuenta {self.numero_cuenta} tu balance es {self.balance}"

    def depositar(self, cantidad_deposito):
        self.balance += cantidad_deposito
        print("Deposito aprobado")

    def retirar(self, cantidad_retiro):
        if self.balance >= cantidad_retiro:
            self.balance -= cantidad_retiro
            print("Retiro aprobado")
        else:
            print("Retiro rechazado")

def crear_cliente():
    nombre = input("Tu nombre?: ")
    apellido = input("Tu apellido?: ")
    numero_cuenta = input("Tu numero de cuenta?: ")
    cliente = Cliente(nombre, apellido, numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()

    while mi_cliente:
        print(mi_cliente)
        retiro_o_deposito = input("Deposito(1)  Retiro(2) Salir(3): ")
        if retiro_o_deposito == "1":
            cantidad_deposito = int(input("Ingrese cantidad del deposito: "))
            mi_cliente.depositar(cantidad_deposito)
        elif retiro_o_deposito == '2':
            cantidad_retiro = int(input("Ingrese cantidad del retiro: "))
            mi_cliente.retirar(cantidad_retiro)
        elif retiro_o_deposito == '3':
            print("Good Bye!!")
            return


inicio()








