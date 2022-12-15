from random import randint

# Presentacion del programa
nombre = input("Cual es tu nombre: ")
print(f"Bienvenido {nombre} he pensado un numero del 1 al 100 y tienes ocho intenteos para adivinar el numero")

# Cuerpo del programa
numero_secreto = randint(1,100)
intentos = 0

while intentos < 8:
    intentos += 1
    print(f"Intento numero {intentos}")
    numero = int(input("Elije un numero: "))
    if numero < 1 or numero > 100:
        print("numero elegido no permitido")
    elif numero < numero_secreto:
        print("respuesta incorrecta, el numero elegido es menor al numero secreto")
    elif numero > numero_secreto:
        print("respuesta incorrecta, el numero elegido es mayor al numero secreto")
    elif numero == numero_secreto:
        print(f"Felicitaciones!, numeros de intentos {intentos}")
        break

if numero != numero_secreto:
    print(f"Buen intento, el numero secreto era {numero_secreto} ")
