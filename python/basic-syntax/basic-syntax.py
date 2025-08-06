#Primera impresión:
print("Hello World")

#Variables:
Nombre = "Juan" #str/string
Edad = 45 #int/entero o float/decimales
Jugando = True #Booleano/True o False

#Obtener la entrada del usuario (input):
Nombre = input("ingrese su nombre:")
Edad = input("Ingrese su edad")
print(Nombre + Edad)

#Type/Convertir tipos de datos a otros/entero a decimal, entero a string:
int()
float()
str()
bool()

# Calculadora basica:
num = float(input("First number:"))
second_num = float(input("Second number:"))

sum_total = num + second_num
print("Suma total: " + str(sum_total))

#String:
Curso = 'Python para novatos'
print(Curso.upper()) #Minusculas a mayusculas/lower() de Mayusculas a minusculas
print(Curso)
print(Curso.find('o')) #Encontrar
print(Curso.replace("para", "por")) #Remplazar 
print('Python' in Curso) #Imprimir 'Python' encontrado en la variable Curso

#Operaciones aritmeticas:
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x = x + 3
x += 3 #Lo mismo que x = x + 3, aplica en todos los signos +-*/

#Prioridad del operador/operator precedence:
x = (10 + 3) * 2
print(x)

#Operadores de comparación/Comparison operators:
x = 3 > 2 #Booleano devuelve True o False/Aplica con todos los comparadores
print(x)
Operadores_comparación = ">, >=, <, <=, ==, !=" #Muy importantes

#Operadores logicos/Logical operators:
Price = 25
print(Price > 10 and Price < 30) #Devuelve True o False dependiendo del resultado
print(Price > 10 or Price < 30) #Lo mismo

#Declaraciones If:
temperatura = 35

if temperatura > 30: #si temperatura es mayor a 30 entonces
    print("It´s a hot day")
    print("Drink plenty of water")
elif temperatura > 20:
    print("It´s a nice day")
elif temperatura > 10:
    print("It´s a bit cold")
else:
    print("It´s cold")

#Ejercicio/Exercise:
weight = float(input("Weight:"))
unit = input("(K)g or (L)bs:")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

#Bucles while/While loops:
i = 1
while i <= 5: #Mientras i sea menos o igual a 5, seguir el bucle
    print(i)
    i = i + 1

#Listas/Lists:
nombres = ["Joel", "Valentin", "Jav", "Shavl"] #Esto es una lista de nombres
print(nombres[0])
print(nombres[-1])
print(nombres[0:3]) #Obtener desde el primer al tercer valor de la lista
print(nombres)

#Métodos de lista/List methods:
numbers = [1, 2, 3, 4, 5]
numbers.append(6) #append() inserta un dato a la lista
print(numbers)
numbers.insert(0, -1) #Insertar un dato en una ubicación del index específica
print(numbers)
numbers.remove(3) #Elimina o remueve un dato de la tabla 
print(numbers)
numbers.clear() #Limpia la lista/elimina todos los datos
print(numbers)
print(2 in numbers) #Verifica si esta el número 2 en la lista numbers
print(len(numbers)) #len()Devuelve el número de elementos que hay en la lista

#Bucles For/For loops:
Números = [1, 2, 3, 4, 5, 6, 7, 8]
print(Números)
for item in Números: #Iterar por cada dato de la lista uno por uno
    print(item)

i = 0
while i < len(Números): #Lo mismo que el bucle For pero While
    print(Números[i])
    i = i + 1

#La función rango()/The range() Function:
numeros_2 = range(5, 10, 2) #range()Crear un rango entre un número con otro número
print(numeros_2)
for number in numeros_2:
    print(number)

#Tuplas/Tuples:
numerables = (1, 2, 3, 3, 3) #Esta es una tupla, inmutable, no modificable
numerables.count(3) #Devuelve la cantidad de veces que se repite un dato
numerables.index(3) #Devuelve el index de la primera aparición del dato dado

#Diccionarios/Diccionaries:
Mercado = {"Papalla":"12.5", "Pera":"4.00"} #Diccionario, contiene una llave con un valor
print(Mercado)

#Excepciones/Exceptions:
try: #try: intenta un bloque de codigo y si sale mal(excepción) hace algo(mensaje de error)
    first = 10
    second = 0

    resultado = first / second
    
    print(resultado)
except:
    print("Error: Denominator cannot be 0.")

#Funciones/Functions definir y llamar:
def functionName(): #Definir función
    print("Hello World")

functionName() #Llamar función

