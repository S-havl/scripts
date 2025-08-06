#Primera impresión: 1
#1
# nombre = input("Escribe tu nombre: ")
# print("Hola", nombre)
#2
# nombre = input("Escribe el nombre: ")
# print("Buenos días", nombre)
# print("Buenas tardes", nombre)
# print("Buenas noches", nombre)
#3
# Curso_fav = input("Curso favorito: ")
# Duración = input("Duración del curso: ")
# print(Curso_fav, Duración)
#4
# nombre = input("Ingrese su nombre: ")
# print("Bienvenido", nombre)
#5
# print("Lo que no te mata, te hace más fuerte. \n--Alberto Extinto.")
#Variables: 2
#1
# Nombre = "Shavl"
# Edad = 15
# Ciudad = "New York"
# print(Nombre, str(Edad), Ciudad)
#2
# Edad = 15
# print(Edad + 10)
#3
# Jugando = True
# print(Jugando)
# Jugando = False
# print(Jugando)
#4
# Metros = float(input("Escriba los metros a convertir: "))
# conversion = Metros * 100
# print(conversion)
#5
# Saldo_inicial = float(input("Ingrese su saldo inicial: "))
# Transaccion = float(input("Ingrese la cantidad a transferir: "))
# restante_total = Saldo_inicial - Transaccion
# print(restante_total)
#Obtener entrada del usuario(input): 3
#1
# Color_usuario = input("Ingrese su color favorito: ")
# Comida_usuario = input("Ingrese su comida favorita: ")
# print("Su color favorito es el", Color_usuario, "Y su comida favorita es", Comida_usuario)
#2
# Fecha_nacimiento = int(input("Ingrese su fecha de nacimiento: "))
# Fecha_actual = int(input("Ingrese la fecha actual: "))
# Edad = Fecha_actual - Fecha_nacimiento
# print("Su edad actual es:", Edad)
#3
# Grados_Celsius = int(input("Ingrese los grados C° a convertir: "))
# Conversion = (Grados_Celsius * 9/5) + 32
# print(Grados_Celsius, "a fahrenheit", Conversion)
#4
# Palabra = input("Ingrese una palabra: ")
# Num = input("Ingrese un número: ")
# Contraseña = Palabra + Num
# print("Su contraseña creada es:", Contraseña)
#5
# Horas_dormir = float(input("Ingrese la cantidad de horas que duerme: "))
# Horas_trabajar = float(input("Ingrese las horas que trabaja: "))
# Horas_restantes = 24 - (Horas_dormir + Horas_trabajar)
# print("Le queda de tiempo libre estas horas:", Horas_restantes)
#Type/Convertir tipos de datos: 4
#1
# Numero = input("Escriba un número: ")
# int(Numero)
# print("Número convertido a entero", Numero)
#2
# Numero_entero = int(input("Ingrese un número: "))
# Conversión = float(Numero_entero)
# print("Su número convertido a flotante es:", Conversión)
#3
# Numero_flotante = float(input("Ingrese un número decimal: "))
# Conversion = str(Numero_flotante)
# print("Su número convertido a cadena(string)es:", Conversion, type(Conversion))
#4
# Booleano = input("Ingrese True o False: ")
# Conversion = bool(Booleano)
# print("Su valor convertido a booleano es", Conversion, type(Conversion))
#5
# Num1 = str(input("Ingrese el primer número: "))
# Num2 = str(input("Ingrese el segundo número: "))
# Suma = int(Num1) + int(Num2)
# print("La suma total es", Suma)
#Calculadora básica: 5
#1
# Num1 = float(input("Ingrese el primer número: "))
# Num2 = float(input("Ingrese el segundo número: "))
# Diferencia = Num1 - Num2
# print("Resultado de la resta:", Diferencia)
#2
# Num1 = float(input("Ingrese el primer número: "))
# Num2 = float(input("Ingrese el segundo número: "))
# Producto = Num1 * Num2
# print("El resultado de la multiplicación es:", Producto)
#3
# try:
#     Num1 = float(input("Ingrese el primer número: "))
#     num2 = float(input("Ingrese el segundo número: "))
#     Resultado = Num1 / num2
#     print("El resultado de la división es:", Resultado)
# except:
#     if num2 == 0:
#         print("Error: No se puede dividir por 0.")

#4
# def sumar(num1, num2):
#     return num1 + num2

# def restar(num1, num2):
#     return num1 - num2

# def multiplicar(num1, num2):
#     return num1 * num2

# def dividir(num1, num2):
#     return num1 / num2

# def main():
#     print("Elije una opción:")
#     print("1. Sumar")
#     print("2. Restar")
#     print("3. Multiplicar")
#     print("4. Dividir")

#     Seleccion = input("Selección: ")

#     if Seleccion == '1':
#         num1 = float(input("Ingrese el primer número: "))
#         num2 = float(input("Ingrese el segundo número: "))
#         Suma = sumar(num1, num2)
#         print(Suma)

#     if Seleccion == '2':
#         num1 = float(input("Ingrese el primer número: "))
#         num2 = float(input("Ingrese el segundo número: "))
#         Resta = restar(num1, num2)
#         print(Resta)

#     if Seleccion == '3':
#         num1 = float(input("Ingrese el primer número: "))
#         num2 = float(input("Ingrese el segundo número: "))
#         Producto = multiplicar(num1, num2)
#         print(Producto)

#     if Seleccion == '4':
#         try:
#             num1 = float(input("Ingrese el primer número: "))
#             num2 = float(input("Ingrese el segundo número: "))
#             Resultado = dividir(num1, num2)
#             print(Resultado)
#         except:
#             if num2 == 0:
#                 print("Error, no puede dividir por cero 0.")

# main()
#5
# def sumar(num1, num2):
#     return num1 + num2

# def restar(num1, num2):
#     return num1 - num2

# def multiplicar(num1, num2):
#     return num1 * num2

# def dividir(num1, num2):
#     return num1 / num2

# def main():
#     Historial = []
#     while True:
#         print("Elije una opción:")
#         print("1. Sumar")
#         print("2. Restar")
#         print("3. Multiplicar")
#         print("4. Dividir")

#         Seleccion = input("Selección: ")

#         if Seleccion == '1':
#             num1 = float(input("Ingrese el primer número: "))
#             num2 = float(input("Ingrese el segundo número: "))
#             Suma = sumar(num1, num2)
#             Historial.append(Suma)
#             print(Suma)

#         if Seleccion == '2':
#             num1 = float(input("Ingrese el primer número: "))
#             num2 = float(input("Ingrese el segundo número: "))
#             Resta = restar(num1, num2)
#             Historial.append(Resta)
#             print(Resta)

#         if Seleccion == '3':
#             num1 = float(input("Ingrese el primer número: "))
#             num2 = float(input("Ingrese el segundo número: "))
#             Producto = multiplicar(num1, num2)
#             Historial.append(Producto)
#             print(Producto)

#         if Seleccion == '4':
#             try:
#                 num1 = float(input("Ingrese el primer número: "))
#                 num2 = float(input("Ingrese el segundo número: "))
#                 Resultado = dividir(num1, num2)
#                 Historial.append(Resultado)
#                 print(Resultado)
#             except:
#                 if num2 == 0:
#                     print("Error, no puede dividir por cero 0.")
#         elif Seleccion == '0':
#             print(f"\nHistorial de resultados:")
#             print(Historial)
#             break
                 
# if __name__ == "__main__":
#     main()

#String: 6
#1
# Nombre = input("Ingrese su nombre: ")
# Mayus = Nombre.upper()
# print("Su nombre en mayúsculas:", Mayus)
#2
# def contar_vocales(cadena):

#     vocales = "aeiouAEIOU"
#     contador = 0

#     for i in cadena:
#         if i in vocales:
#             contador += 1

#     return contador

# cadena = input("Escribe una frase: ")
# vocales = contar_vocales(cadena)

# print("Vocales de tu frase:", vocales)

#3
# frase_usuario = input("Ingrese una frase: ")
# palabra_remplazo = input("Ingrese la palabra a remplazar: ")

# frase_remplazada = frase_usuario.replace(palabra_remplazo, "mucho")
        
# print("Frase remplazada:", frase_remplazada)
        
#4
# frase = "hola mundo"
# palabra_usuario = input("Ingrese la palabra: ")

# if palabra_usuario in frase:
#     print("Si está.")
# else:
#     print("No está.")

#5
# Cadena_usuario = input("Ingrese una frase(cadena): ")

# Cadena_invertida = Cadena_usuario[::-1]

# print("Tu cadena o frase invertida:", Cadena_invertida)

#Operaciones aritméticas: 7
#1
# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))
# num3 = float(input("Ingrese el tercer número: "))
# promedio = (num1 + num2 + num3) / 3
# print("El promedio de los números ingresados es:", promedio)

#2
# base = float(input("Ingrese la base del triángulo: "))
# altura = float(input("Ingrese la altura del triángulo: "))
# Área = (base * altura) / 2
# print("El área del triángulo es:", Área)

#3
# porcentaje = float(input("Ingrese el porcentaje: "))
# numero = float(input("Ingrese el número: "))
# total = (porcentaje / 100) * numero
# print("El", porcentaje, "por ciento de", numero, "es:", total)

#4
# Primer_precio = float(input("Ingrese el precio: "))
# porcentaje = float(input("Ingrese el porcentaje de aumento: "))
# aumento = (porcentaje / 100) * Primer_precio
# total = Primer_precio + aumento
# print("El precio final con aumento es:", total)

#5
# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))
# num3 = float(input("Ingrese el tercer número: "))
# promedio = (num1 + num2 + num3) / 3

# base = float(input("Ingrese la base del triángulo: "))
# altura = float(input("Ingrese la altura del triángulo: "))
# Área = (base * altura) / 2

# porcentaje = float(input("Ingrese el porcentaje: "))
# numero = float(input("Ingrese el número: "))
# total = (porcentaje / 100) * numero

# Primer_precio = float(input("Ingrese el precio: "))
# porcentaje = float(input("Ingrese el porcentaje de aumento: "))
# aumento = (porcentaje / 100) * Primer_precio
# total2 = Primer_precio + aumento

# print("Primera operación: Promedio:", promedio)
# print("Segunda operación: Área:", Área)
# print("Tercera operación: Total:", total)
# print("Cuarta operación: Total:", total2)

#Operadores de comparación: 8
#1
# Num1 = float(input("Escribe el primer número: "))
# Num2 = float(input("Escribe el segundo número: "))

# if Num1 > Num2:
#     print("El número uno es mayor que el número dos.")
# elif Num2 > Num1:
#     print("El número dos es mayor que el número uno.")

#2
# Cadena_uno = str(input("Ingresa una cadena: "))
# Cadena_dos = str(input("Ingresa una segunda cadena: "))

# if Cadena_uno == Cadena_dos:
#     print("Son iguales.")
# else:
#     print("No son iguales.")

#3
# Edad_usuario = int(input("Ingrese su edad: "))

# if Edad_usuario >= 18:
#     print("Eres mayor de edad.")
# else:
#     print("Eres menor de edad.")

#4
# Cadena1 = str(input("Primera cadena: "))
# Cadena2 = str(input("Segunda cadena: "))

# if len(Cadena1) == len(Cadena2):
#     print("La longitud de las cadenas son iguales.")
# elif len(Cadena1) > len(Cadena2):
#     print("La longitud de la cadena uno es mayor a la de la segunda.")
# elif len(Cadena2) > len(Cadena1):
#     print("La longitud de la cadena dos es mayor a la de la primera.")

#5
# first = int(input("Ingrese el primer número: "))
# second = int(input("Ingrese el segundo númmero: "))

# if first % second == 0:
#     print("El primer número es múltiplo del segundo.")
# else:
#     print("El primer número no es múltiplo del segundo.")

#Operadores lógicos: 9
#1
# Numero = int(input("Ingresa un número: "))

# if Numero in range(0, 11):
#     print("El número ingresado se encuentra en un rango de 0 a 10.")
# else:
#     print("El número ingresado no se encuentra en el rango.")

#2
# número = int(input("Ingrese un número: "))

# if número % 2 == 0 or número > 10:
#     print("Es par o mayor a 10.")
# else:
#     print("No es par, ni mayor a 10")

#3
# Edad_usuario = int(input("Ingrese su edad: "))
# Salario_usuario = float(input("Ingrese su salario: "))

# if Edad_usuario >= 18 and Salario_usuario >= 500:
#     print("Usted es apto para un beneficio!")
# else:
#     print("Usted no es apto para un beneficio.")

#4
# numero_usuario = float(input("Ingrese un número: "))

# if not (numero_usuario < 0):
#     print("No es negativo.")
# else:
#     print("Es negativo.")

#5
# num_usuario = int(input("Ingrese cualquier número: "))

# if not (num_usuario < 0) and num_usuario > 10 or num_usuario > 20:
#     print("Cumple con todo.")
# else:
#     print("No cumple con todo.")

#Declaraciones if: 10
#1
# Temperatura = int(input("Ingrese la temperatura actual (C°): "))

# if Temperatura >= 35:
#     print("Ir a la playa.")
# elif Temperatura < 30 and Temperatura > 15:
#     print("Ir al parque.")
# elif Temperatura < 15:
#     print("Abrigarse.")

#2
# Calificacion = float(input("Ingrese su calificación (0, 20): "))

# if Calificacion == 20:
#     print("Tienes AD.")
# elif Calificacion >= 14:
#     print("Tienes A.")
# elif Calificacion < 14 and Calificacion >= 11:
#     print("Tienes B.")
# elif Calificacion < 11 or Calificacion == 0:
#     print("Tienes C.")

#3
# Compras_realizadas = int(input("Ingrese el número de compras realizadas: "))

# if Compras_realizadas >= 20:
#     print("Tiene un descuentro del 20%.")
# elif Compras_realizadas < 20 and Compras_realizadas > 10:
#     print("Tiene un descuentro del 10%")
# elif Compras_realizadas < 10:
#     print("No tienes ningún descuento.")

#4
# usuario_numero = float(input("Ingrese un número: "))

# if usuario_numero % 2 == 0:
#     print("El número es par.")
# else:
#     print("El número es impar.")

#5
# edad_usuario = int(input("Ingrese su edad: "))

# if edad_usuario < 12:
#     print("Eres niño.")
# elif edad_usuario > 12 and edad_usuario < 18:
#     print("Eres adolescente.")
# elif edad_usuario >= 18 and edad_usuario < 40:
#     print("Eres adulto.")
# elif edad_usuario >= 50:
#     print("Eres anciano.")

#Bucles while: 11
#1
# i = 0
# while i <= 10:
#     print(i)
#     i += 1

#2
# i = 1
# while i <= 100:
#     print(i)
#     i += i

#3
# cuenta_regresiva = 10
# while cuenta_regresiva >= 0:
#     print(cuenta_regresiva)
#     cuenta_regresiva -= 1

#4
# Contraseña_correcta = "teAmoHelen"
# intentos = 0

# while intentos <= 3:
#     Contraseña_ingresada = input("Ingrese la contraseña: ")

#     if Contraseña_ingresada == Contraseña_correcta:
#         print("Contraseña correcta!.")
#         break
#     else:
#         intentos += 1
#         if intentos == 3:
#             print("Se te acabaron los intentos.")
#             break
            
#5
# i = 1
# total = 0

# while i <= 50:
#     if i % 2 == 0:   
#         total += i
#     i +=1

# print("Suma total de números pares:", total)

#Listas: 12
#1
# Compras = ["Pollo", "Arroz", "Pescao", "Mayonesa", "Papa"]
# print(Compras)

#2
# Lista = ["Pollo", "Arroz", "Pescao", "Mayonesa", "Papa"]
# print(Lista[0])
# print(Lista[-1])

#3
# Lista_usuario = ["Pollo", "Arroz", "Pescao", "Mayonesa", "Papa"]
# Sublista = [Lista_usuario[0], Lista_usuario[1], Lista_usuario[2]]
# print(Lista_usuario)
# print(Sublista)

#4
# Lista = ["Pollo", "Arroz", "Pescao", "Mayonesa", "Papa"]
# print(Lista)
# Lista[1] = "Carne"
# print(Lista)

#5
# Lista = ["Pollo", "Arroz", "Pescao", "Mayonesa", "Papa"]
# print(Lista)
# Lista.append("Manzanas")
# print(Lista)
# Lista.remove("Pollo")
# print(Lista)

#Métodos de lista: 13
#1
# Lista_vacia = []
# print(Lista_vacia)
# Lista_vacia.append("Papa")
# Lista_vacia.append("Arroz")
# Lista_vacia.append("Leche")
# Lista_vacia.append("Mantequilla")
# Lista_vacia.append("Carne")
# print(Lista_vacia)

#2
# Lista = ["Pollo", "Arroz", "Pescao", "Mayonesa", "Papa"]
# print(Lista)
# Lista.insert(1, "Helen")
# print(Lista)

#3
# lista = ["Carne", "Pollo", "Pollo", "Fideos", "Pollo", "Pollo", "Pollo"]
# print(lista)
# lista.remove("Pollo")
# print(lista)

#4
# lista = ["Carne", "Pollo", "Pollo", "Fideos", "Pollo", "Pollo", "Pollo"]
# print(lista)
# lista.clear()
# print(lista)

#5
# lista = ["Carne", "Pollo", "Pollo", "Fideos", "Pollo", "Pollo", "Pollo", "Hola", "waza", "Amor"]
# print(len(lista))

#Bucles for: 14
#1
# Mi_lista = ["Helen", "Yazmin", "Torre", "Ramos", "Venus"]

# for elemento in Mi_lista:
#     print(elemento)

#2
# Num_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# suma_total = 0

# for num in Num_lista:
#     print(num)
#     suma_total += num

# print(suma_total)

#3
# Palabra_usuario = str(input("Ingrese una palabra: "))

# for caracter in Palabra_usuario:
#     print(caracter)

#4
# list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in list_num:
#     print(num ** 2)

#5
# cad_lis = ["Hola", "Pato", "Gallina", "Cerdo", "Azul"]

# for cad in cad_lis:
#     print(cad.upper())

#Función range(): 15
#1
# for i in range(10):
#     print(i)

#2
# for i in range(5, 16):
#     print(i)

#3
# for i in range(10, 21, 2):
#     print(i)

#4
# for i in range(10, 0, -1):
#     print(i)

#5
# suma_total = 0
# for i in range(11):
#     suma_total += i

# print(suma_total)

#Tuplas: 16
#1
# Tupla = ("Feliz", "Triste", "Enojado", "Arroz", "Pollo")

# print(Tupla[0])
# print(Tupla[-1])

#2
# Tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10)
# print(Tupla.count(10))

#3
# Tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10)
# print(Tupla.index(9))

#4
# Tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10)

# for i in Tupla:
#     print(i)

#5
# Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
# Tupla = tuple(Lista)
# print(Tupla)

#Diccionarios: 17
#1
# Dic = {"Nombre": "Shavl", "Edad": "9999", "Power": "Inf"}
# print(Dic["Nombre"])

#2
# Dic = {"Nombre": "Shavl", "Edad": "9999", "Power": "Inf"}
# print(Dic)
# Dic["Eye"] = "56"
# print(Dic)

#3
# Dic = {"Nombre": "Shavl", "Edad": "9999", "Power": "Inf"}
# print(Dic)
# del Dic["Nombre"]
# print(Dic)

#4
# Dic = {"Nombre": "Shavl", "Edad": "9999", "Power": "Inf"}
# for clave, valor in Dic.items():
#     print(clave, valor)

#5
# Dic = {"Nombre": "Shavl", "Edad": "9999", "Power": "Inf"}
# clave = input("Escribe la clave: ")

# if clave in Dic:
#     print("Si existe.")
# else:
#     print("No existe.")

#Excepciones: 18
#1
# def division(num1, num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         print("No se puede dividir por 0 cero.")

# num1 = float(input("Ingrese el primer número"))
# num2 = float(input("Ingrese el segundo número: "))

# total = division(num1, num2)
# print(total)

#2
# def soliticar_num():
#     while True:
#         try:
#             numero = float(input("Ingrese un número: "))
#         except ValueError:
#             print("Valor incorrecto.")

# soliticar_num()

#3
# try:
#     open('Hola.jpg')
# except FileNotFoundError:
#     print("El archivo no existe")

#4
# lista = [1, 2, 3, 4, 5, 6]

# def acceder(index):
#     while True:
#         try:
#             print(lista[index])
#             break
#         except IndexError:
#             print("El indice ingresado no existe.")
#             break

# indice_usuario = int(input("Ingrese el indice al que desee acceder: "))
# acceder(indice_usuario)

#5
# def multiplicar():
#     while True:
#         try:
#             num1 = float(input("Ingrese un número: "))
#             num2 = float(input("Ingrese otro número: "))
#             resultado = num1 * num2

#             print(resultado)
            
#         except ValueError:
#             print("Error: Ingrese solo números.")

# multiplicar()
            
#Funciones: 19
#1
# def saludo(nombre):
#     print("Buenos días", nombre)

# nombre_usuario = str(input("Ingrese su nombre: "))
# saludo(nombre_usuario)

#2
# def sumar(a, b):
#     return a + b

# num1 = float(input("Primer número: "))
# num2 = float(input("Segundo número: "))

# total = sumar(num1, num2)
# print("El total de la suma es:", total)

#3
# def conversion(celsius):
#     return (celsius * 9/5) + 32

# celsius = float(input("Grados celsius: "))
# conversión = conversion(celsius)
# print("Celsius a Fahrenheit:", conversión)

#4
# def factorial(n):
#     if n < 0:
#         raise ValueError("El factorial no está definido para números negativos.")
    
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
    
#     return result

# n_usuario = int(input("Ingrese el n: "))
# fact = factorial(n_usuario)
# print(fact)

#5
def verificar(n):

    if n % 2 == 0:
        print("Es par")
    else:
        print("Es inpar")

n_user = int(input("Ingrese el número a verificar: "))

verificar(n_user)

#fin.