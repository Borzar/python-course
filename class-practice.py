class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa("blanco", 4)


class Cubo:
    def __init__(self, color):
        self.color = color

    caras = 6

cubo_rojo = Cubo('rojo')

class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje("Humano", True, 17)

class Perro:
    def ladrar(self):
        print("Guau!")

dalton = Perro()
dalton.ladrar()

class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo()

class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

mialarma = Alarma()
mialarma.postergar(30)


class Mascota: 
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Mascota.respirar()

class Jugador:

    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True 

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

boris = Alumno('Boris', 31)


class Pajaro:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre 
        self.cantidad_patas = cantidad_patas 

class Paloma(Pajaro):
    pass

tututu = Paloma(10, 'Dalton', 4)


class Vehiculo:
    def acelerar(self):
        pass
    
    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass


palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for mi_item in [palabra, lista, tupla]:
    print(len(mi_item)) 

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

legolas = Arquero()
gandalf = Mago()
samuraiX = Samurai()

personajes = [legolas, gandalf, samuraiX]

for personaje in personajes:
    personaje.atacar()
