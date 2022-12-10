import random

# lista de opciones
palabras_secretas = ["arbol", "casa", "lentes", "oro", "soga","vaso", "mouse"]
palabra_sercreta = random.choice(palabras_secretas)
palabra_secreta_length = len(palabra_sercreta)

# Bienvenida
print("************************\n")
print("BIENVENIDO AL JUEGO")
print(f"La palabra tiene {palabra_secreta_length} caracteres\n")
print("************************\n")

# listas globales
correctas = []
incorrectas = []
palabra_sercreta_mostrar_usuario = []

def actualizar_guiones_al_usuario(palabra_sercreta, letra_ingresada):
    for letra in palabra_sercreta:
        if letra == letra_ingresada:
            ingresada = palabra_sercreta_mostrar_usuario.append(palabra)
            print(ingresada)
        print(letra)


def mostrar_guiones_al_usuario(palabra_sercreta):
    for letras in palabra_sercreta:
        guiones = letras.replace(letras, "-")
        palabra_sercreta_mostrar_usuario.append(guiones)
    return print(palabra_sercreta_mostrar_usuario)

def turnos():
    print(f"PALABRA SECRETA: {palabra_sercreta}")
    mostrar_guiones_al_usuario(palabra_sercreta)
    for turnos in range(1,9):
        print(f"Turno {turnos}")
        letra = input("Ingresa alguna letra: ")
        resultado = palabra_sercreta.find(letra)

        if resultado >= 0:
            correctas.append(letra)
            if len(correctas) == len(palabra_sercreta):
                return print("Has Ganado !!")
            else:
                pass

        else:
            incorrectas.append(letra)
            if len(incorrectas) == 6:
                return print("Has perdido !!")
            else:
                pass

    return print("fin de juego")


# Debug
print("************************")
print(f"PALABRA SECRETA: {palabra_sercreta}")
print(f"CORRECTAS: {correctas}")
print(f"INCORRECTAS: {incorrectas}")

