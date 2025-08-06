#Ejercicios variables:
Mi_nombre = "S-havl"
Edad = 15
Estudiando = True
Altura = 1.61
Pareja = "Venus"
EsFeliz = True

#Ejercicios input(entrada del usuario):
nombre_usuario = input("Escribe tu nombre: ")
print(nombre_usuario)
Edad_usuario = input("Escribe tu edad: ")
print("Tienes " + Edad_usuario + " años")
Color_favorito = input("Escribe tu color favorito: ")
print("Tu color favorito es el " + Color_favorito)
Comida_favorita = input("Escribe tu comida favorita: ")
print("Tu comida favorita es " + Comida_favorita)
Deporte_favorito = input("Escribe tu deporte favorito: ")
print("El deporte favorito de " + nombre_usuario + " es " + Deporte_favorito)

#Ejercicios Type/Convertir tipos de datos:
número_entero = 56
print(str(número_entero))
Cadena = "1.61"
print(float(Cadena))
Feliz = True
print(str(Feliz))
cadena_entero = "45"
print(int(cadena_entero))
num_flotante = 1.45555
print(int(num_flotante))

#Ejercicios de calculadora básica:
número_one = input("Escribe el primer número: ")
número_two = input("Escribe el segundo número: ")
suma_total = float(número_one) + float(número_two)
print(float(suma_total))

número_one = input("Escribe el primer número: ")
número_two = input("Escribe el número dos: ")
resta_total = float(número_one) - float(número_two)
print(float(resta_total))

número_one = input("Escribe el primer número: ")
número_two = input("Escribe el segundo número: ")
producto_total = float(número_one) * float(número_two)
print(float(producto_total))

número_one = input("Escribe el primer número: ")
número_two = input("Escribe el segundo número: ")
Cociente_total = float(número_one) / float(número_two)
print(float(Cociente_total))

número_one = input("Escribe el primer número: ")
número_two = input("Escribe el segundo número: ")
Potencia_total = float(número_one) ** float(número_two)
print(float(Potencia_total))

#Ejercicios de string:
cadena_usuario = input("Escribe una palabra o frase aleatoria: ")
print(cadena_usuario.upper())
cadena_usuario = input("Escribe aleatoriamente en mayúsculas: ")
print(cadena_usuario.lower())
cadena_usuario = input("Escribe palabras con la letra A: ")
print(cadena_usuario.find('a'))
cadena_usuario = input("Escribe palabras con muchas E: ")
print(cadena_usuario.replace("e", "3"))
cadena_usuario = input("Escribe: ")
print('Python' in cadena_usuario)

#Ejercicios operaciones aritméticas:
print(15 + 7)
print(20 - 4)
print(5 * 6)
print(10 / 2)
print(2 ** 3)

#Ejercicios operadores comparativos:
print(10 > 5)
print(3 < 8)
print(7 == 7)
print(6 != 9)
print(4 >= 4)

#Ejercicios operadores lógicos:
print(5 > 3 and 3 < 10)
print(2 < 1 or 2 > 0)
print(7 > 3 and 7 < 10)
print(4 < 2 or 4 > 3)
print(not 5 < 3)

#Ejercicios declaraciones if:
Usuario_temperatura = int(input("Escribe una temperatura: "))
if int(Usuario_temperatura) > 30:
    print("It´s a cool day")

Usuario_temperatura = int(input("Temperatura: "))
if int(Usuario_temperatura) <= 20:
    print("It´s a cool day")

Usuario_numero = int(input("Escribe un número entero: "))
if int(Usuario_numero) < 0:
    print("El número es negativo")
elif int(Usuario_numero) > 0:
    print("El número es positivo")
else:
    print("El número es cero")

Usuario_edad = int(input("Escriba su edad: "))
if int(Usuario_edad) >= 18:
    print("Puede votar")
else:
    print("No puede votar")

Usuario_calificación = float(input("Escriba su calificación: "))
if float(Usuario_calificación) >= 90:
    print("A")
elif float(Usuario_calificación) >= 80 and float(Usuario_calificación) < 90:
    print("B")
elif float(Usuario_calificación) >= 70 and float(Usuario_calificación) < 80:
    print("C")
elif float(Usuario_calificación) < 70:
    print("F")

#Ejercicios while loops:
i = 1
while i <= 5:
    print(i)
    i = i + 1

i = 10
while i >= 1:
    print(i)
    i -= 1

i = 2
while i <= 10:
    print(i)
    i += 2

i = 0
while i <= 3:
    print("Hola")
    i += 1

suma = 0
i = 1
while i <= 10:
    suma += i
    i += 1

print("El resultado de la suma total es: " + str(suma))

#Ejercicios listas:
Colores = ["Azul", "Rojo", "Morado"]
print(Colores)

Colores.append("Verde")
print(Colores)

Colores.remove("Azul")
print(Colores)

print(Colores[1])

Colores[-1] = "Naranja"
print(Colores)

#Ejercicios métodos de lista:
Five_numbers = [1, 2, 3, 4, 5]
print(Five_numbers)

Five_numbers.append(6)
print(Five_numbers)

Five_numbers.insert(0, 0)
print(Five_numbers)

Five_numbers.remove(2)
print(Five_numbers)

Five_numbers.clear()
print(Five_numbers)

print(len(Five_numbers))

#Ejercicios bucles for:
string = "Hola Mundo"
for item in string:
    print(item)

contar = [1, 2, 3, 4, 5, 6]
for item in contar:
    print(item)

numeros =   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_total = 0
for numero in numeros:
    suma_total += numero

print(suma_total)

for numeros in range(1, 6):
    print(numeros)

for interar in range(10, 0, -1):
    print(interar)

#Ejercicios función range():
for object in range(5):
   print(object)

for num in range(5, 11):
    print(num)

for v in range(10, 0, -1):
    print(v)

for c in range(2, 11, 2):
    print(c)

for a in range(1, 10, 2):
    print(a)

#Ejercicios tuplas:
Frutas = ("Manzana", "Platano", "Naranja")
print(Frutas)

tupla_num = (1, 2, 2, 2, 2, 2, 2, 3, 4, 5)
print(tupla_num.count(2))

print(tupla_num.index(4))

print(tupla_num)

#Ejercicios diccionarios:
Diccionario = {"Amada" : "Helen", "Edad" : "15", "Pan" : "1.56"}
print(Diccionario)

Diccionario["Jamon"] = "4.56"
print(Diccionario)

Diccionario["Pan"] = "2.00"
print(Diccionario)

print(Diccionario.pop("Amada"))

for llave in Diccionario:
    print(llave)

#Ejercicios excepciones:
try:
    numero1 = 10
    numero2 = 0
    print(numero1 / numero2)
except:
    print("El número no puede dividirse por 0")

try:
    numero_usuario = int(input("Escriba un número entero: "))
    print(numero_usuario)
except:
    print("El número que ingreso no es entero.")

try:
    with open ('archivo_inexistente', 'r') as file:
        contenido = file.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
except Exception as e:
    print(f"ocurrió un error inesperado: {e}")

try:
    cadena = input("Escribe una cadena(texto): ")
    print(int(cadena))
except:
    print("La cadena no es númerica.")

try:
    lista = [1, 2, 3, 4]
    print(lista[7])
except:
    print("El index no existe.")

#Ejercicios funciones:
def holaMundo():
    print("Hello World")

holaMundo()

def name(nombre):
    print(nombre)

name("S-havl")

def sumar(num1, num2):
    total = num1 + num2
    return total

suma = sumar(5, 8)
print(suma)

def encontrar_maximo(lista_numeros):
    if not lista_numeros:
        return None
    
    maximo = lista_numeros[0]

    for numero in lista_numeros:
        if numero > maximo:
            maximo = numero

    return maximo

numeros = [1, 2, 3, 4, 5]
print(encontrar_maximo(numeros))

def Mayus(cadena):
    return cadena.upper()

cadena = "hola wao"
resultado = Mayus(cadena)
print(resultado)