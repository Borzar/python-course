import random

### while
# numero = 50

# while numero >= 0:
    # if numero % 5 == 0:
        # print(numero)
    # numero -= 1


# lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]


# for numeros in lista_numeros:
    # if numeros >= 0:
        # print(numeros)
    # else:

### range
# Práctica Rango 3
# Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados.
# Para ello:
# Crea un rango de valores que puedas recorrer en un loop
# Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional).
# Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.       # break

# suma_cuadrados = 0
# valores = list(range(1,16))

# for valor_inicial in valores:
    # suma_cuadrados += valor_inicial**2 
    # print(suma_cuadrados)
### enumerate
# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# for indice,nombre in enumerate(lista_nombres):
    # print(f'{nombre} se encuentra en el índice {indice}')

# lista_indices = list(enumerate("Python"))
# print(lista_indices)

# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# for indice,nombre in enumerate(lista_nombres):
    # if nombre.startswith("M"):
        # print(indice)

### zip
# capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
# paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

# for capital, pais in list(zip(capitales,paises)):
    # print(f"la capital de {pais} es {capital}") 

# marcas = ["dell","hp","acer", "samsung"]
# productos = ["monitor", "parlantes", "audifonos", "microfono"]

# zip(marcas, productos)
# print(zip)


# 1: uno / um / one
# 2: dos / dois / two
# 3: tres / três / three
# 4: cuatro / quatro / four
# 5: cinco / cinco / five

# español = ["uno", "dos", "tres", "cuatro", "cinco"]
# portugues = ["um", "dois", "três", "quatro", "cinco"]
# ingles = ["one", "two", "three", "four", "five"]

# numeros = list(zip(español,portugues,ingles)) 
# print(numeros)

# lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

# valor_manximo = max(lista_numeros)
# print(valor_manximo)

# Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:

# lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

# rango =  max(lista_numeros) - min(lista_numeros)
# print(rango)

# Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:
# Almacena dicho valor en una variable llamada edad_minima.
# También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre.

# diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
# edad_minima = min(diccionario_edades.values())
# ultimo_nombre = max(diccionario_edades)
# nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
# aleatorio = choice(nombres)
# print(aleatorio)
# pies = [10, 20, 30, 40, 50]
# metro = 3.2 

# for metros in pies:
    # resultado = metros*metro
    # print(resultado)

# valores = [1, 2, 3, 4, 5, 6, 9.5] 
# # valores_pares = []

# # for n in valores:
    # # if n % 2 == 0:
        # # valores_pares.append(n)
# # print(valores_pares)

# valores_pares = [x for x in valores if x % 2 == 0]
# print(valores_pares)

# Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius. La conversión entre tipo de unidades es la siguiente:
# °C = (°F - 32) * (5/9)
# o expresado de otro modo:
# (grados_fahrenheit-32)*(5/9)
# La lista de temperaturas es la siguiente:
# temperatura_fahrenheit = [32, 212, 275] 
# Almacena esta nueva lista en una variable llamada grados_celsius

# temperatura_fahrenheit = [32, 212, 275]
# temperatura_celcius = []

# for x in temperatura_fahrenheit:
    # celsius = (x-32)*(5/9) 
    # temperatura_celcius.append(celsius)
    # print(temperatura_celcius)

# temperatura_celcius = [x for x in temperatura_fahrenheit]
# print(temperatura_celcius)

# cadena = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:%_#')
# print(cadena)

# frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
# frutas.insert(4, "naranja")
# print(frutas)

# marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

# conjuntos_aislados = marcas_tv = {"Sony", "Philips", "Samsung", "LG"}.isdisjoint(marcas_smartphones)
# print(conjuntos_aislados)


# def bienvenida(nombre_persona):
    # print(f"¡Bienvenido {nombre_persona}!")

# bienvenida('Boris')


# Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

# Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

# También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como argumento a la función creada.

# Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos.

# palabra = "python" 

# def invertir_palabra(palabra):
    # return palabra[::-1].upper()
# print(invertir_palabra(palabra))

# lista_numeros = [2, 1, 4]

# def todos_positivos(lista_numeros):
    # for n in lista_numeros:
        # if n < 0:
            # return False 
        # else:
           # pass 
    # return True

# resultado = todos_positivos(lista_numeros)
# print(resultado)

# lista_numeros = [2,3,4,5]

# def suma_menores(lista_numeros):
    # suma = 0
    # for n in lista_numeros:
        # if n in range(0, 1000):
            # suma = suma + n
        # else:
            # pass
    # return suma 

# resultado = suma_menores(lista_numeros)
# print(resultado)

# lista_numeros = [1,2,3,4]

# def cantidad_pares(lista_numeros):
    # elementos = []
    # for n in lista_numeros:
        # if (n%2==0):
           # elementos.append(n)
        # else:
            # pass
    # return len(elementos)

# resultado = cantidad_pares(lista_numeros)
# print(resultado)

# Práctica sobre Interacción entre Funciones 1
# Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

# La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

# Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

# Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

# Si la suma es menor o igual a 6:

# "La suma de tus dados es {suma_dados}. Lamentable"

# Si la suma es mayor a 6 y menor a 10:

# "La suma de tus dados es {suma_dados}. Tienes buenas chances"

# Si la suma es mayor o igual a 10:

# "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.


# def lanzar_dados():
    # return random.randint(1,6), random.randint(1,6)

# def evaluar_jugada(parametro1, parametro2):
    # suma_dados = parametro1 + parametro2
    # if suma_dados <= 6:
        # return f"La suma de tus dados es {suma_dados}. Lamentable"
    # elif suma_dados > 6 and suma_dados < 10:
        # return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    # elif suma_dados >= 10:
        # return f"La suma de tus dados es {suma_dados}. Parecere una juagada ganadora"


# def reducir_lista(lista):
    # delete_duplicates = list(set(lista))
    # delete_duplicates.remove(max(delete_duplicates))
    # return delete_duplicates 

# def promedio(lista):
    # suma = 0
    # resultado = 0
    # for valores in lista:
        # suma += valores 
    # resultado = suma/len(lista)
    # return resultado

# moneda = ["Cara", "Cruz"]

# def lanzar_moneda():
    # return random.choice(moneda)

# fn_moneda = lanzar_moneda()
# lista_numeros = [1,2,3,4,5]

# def probar_suerte(fn_moneda, lista):
    # if fn_moneda == "Cara":
        # print("La lista se autodestruirá")
        # return []
    # else:
       # print("La lista fue salvada")
       # return lista


# probar_suerte(fn_moneda, lista_numeros)





# def lanzar_moneda():
    # resultado = random.choice(["Cara", "Cruz"])
    # return resultado
 
# def probar_suerte(moneda, lista):
    # if moneda == "Cara":
        # print("La lista se autodestruirá")
        # return []
    # elif moneda == "Cruz":
        # print("La lista fue salvada")
        # return lista


# def numeros_personas(nombre, *args):
    # suma_numeros = sum(args)
    # return f'{nombre}, la suma de tus numeros es {resultado}'

# # numeros_personas('Boris', 4,5,)


# def numeros_persona(nombre, *args):
    # suma_numeros = sum(args)
    # print f'{nombre}, la suma de tus números es {suma_numeros}'

# numeros_persona('Boris', 10,10)


# def cantidad_atributos(**kwargs):
    # cantidad = 0
    # for n in kwargs.items():
        # cantidad += 1 
    # return cantidad 
    
# print(cantidad_atributos(c=3, x=2))

# def lista_atributos(**kwargs):
    # for valores in kwargs:
        # lista = list(kwargs.values())
    # return lista 

# print(lista_atributos(c=2, x=3))

# def describir_persona(nombre, **kwargs):
    # print(f"Características de {nombre}: ")
    # for valores in kwargs:
        # print(valores)
        # print(kwargs.values())

# print(describir_persona('Boris', c=1, d=2))

# 1
# def devolver_distintos(num1, num2, num3):
    # suma = num1 + num2 + num3 
    # mayor = max(num1, num2, num3)
    # menor = min(num1, num2, num3)
    # valor_intermedio = (num1 + num2 + num3) - menor - mayor 
    
    # if suma > 15:
        # print(mayor)
        # return mayor
    # elif suma < 10:
        # print(menor)
        # return menor
    # elif suma >= 10 and suma <= 15:
        # print(valor_intermedio)
        # return valor_intermedio

# devolver_distintos(10,1,3)


# 2 
# lista = []

# def mifuncion(palabra):
    # order = set(palabra)
    # for valores in order:
        # lista.append(valores)
    # lista.sort()
    # return lista

# print(mifuncion('entretenido'))


def funcion_cero(*args):
    for valores in groupby(args) :
        print(valores)


print(funcion_cero(1,2,3,3,4,4))



























