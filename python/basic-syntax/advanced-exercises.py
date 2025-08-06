#Primera impresión: 1
#Generador de mensajes personalizados
# lista_nombres = ["Helen", "Yazmin", "Shavl", "Jav", "Venus"]

# for nombre in lista_nombres:
    
#     mensaje = f"Buendos días, {nombre}!"

#     print(mensaje)

#Variables: 2
#Gestión de presupuesto personal
# def main():
#     Presupuesto_inicial = float(input("Ingrese su presupuesto inicial: "))
#     presupuesto_restante = Presupuesto_inicial

#     while True:
#         categoria_gasto = input("Ingrese la categoria de gasto o fin para terminar el programa: ").strip().lower()

#         if categoria_gasto == 'fin':
#             break

#         if categoria_gasto not in ["comida", "hijos", "colegio"]:
#             print("Ingrese una categoria valida.")
#             continue

#         cantidad_gasto = float(input(f"Ingrese la cantidad gastada en {categoria_gasto}: "))

#         if cantidad_gasto > presupuesto_restante:
#             print(f"Presupuesto insuficiente para {cantidad_gasto}")
#         else:
#             presupuesto_restante -= cantidad_gasto

#         gasto_total = presupuesto_restante - Presupuesto_inicial

#         print("Registro:")
#         print(f"Gasto total: {gasto_total}")
#         print(f"Dinero restante: {presupuesto_restante}")

# main()

#Obtener la entrada del usuario: 3
#Cuestionario interactivo
# def main():

#     nombre = input("Ingrese su nombre: ")

#     while not nombre:
#         print("Debe ingresar su nombre.")
#         nombre = input("Ingrese su nombre: ")

#     edad = input("Ingrese su edad: ")

#     while not edad:
#         print("Debe ingresar su edad.")
#         edad = input("Ingrese su edad: ")

#     ciudad = input("Ingrese su ciudad: ")

#     while not ciudad:
#         print("Debe ingresar su ciudad.")
#         ciudad = input("Ingrese su ciudad: ")

#     print("Registro:")
#     print(f"Nombre: {nombre}")
#     print(f"Edad: {edad}")
#     print(f"Ciudad: {ciudad}")

# main()

#Type/Convertir tipos de datos: 4
#Conversor de temperatura
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# def main():
#     print("Bienvenido al conversor de temperatura celsius-fahrenheit.")
#     print("1. Celsius a fahrenheit.")
#     print("2. Fahrenheit a celsius.")

#     choice = input("Seleciona una de las dos opciones, 1 o 2: ")

#     if choice == '1':
#         celsius = float(input("Ingrese los grados celsius: "))
#         fahrenheit = celsius_to_fahrenheit(celsius)
#         print(f"Los grados {celsius} a fahrenheit {fahrenheit}.")

#     elif choice == '2':
#         fahrenheit = float(input("Ingrese los grados fahrenheit: "))
#         celsius = fahrenheit_to_celsius(fahrenheit)
#         print(f"Los grados fahrenheit {fahrenheit} a celsius {celsius}")

#     else:
#         print("Ingrese una selección valida.")

# main()

#Calculadora básica: 5
#Calculadora de promedio
# calificaciones = input("Ingrese las calificaciones: ")

# calificaciones_lista = calificaciones.split()

# calificaciones_float = [float(calificacion) for calificacion in calificaciones_lista]

# promedio = sum(calificaciones_float) / len(calificaciones_float)

# print(f"El promedio de las calificaciones es: {promedio}")

#String: 6
#Analizador de texto
# texto_usuario = input("Ingrese un texto: ")

# palabras = texto_usuario.split()
# numero_palabras = len(palabras)
# print(f"El número de palabras del texto es: {numero_palabras}")

# palabra_mas_larga = max(palabras, key=len)
# print(f"La palabra más larga del texto es: {palabra_mas_larga}")

# modificacion = texto_usuario.replace("Python", "Programación")
# print(f"El texto modificado es: {modificacion}")

#Operaciones aritméticas: 7
#Calculadora de IMC(Índice de Masa Corporal)
# peso_usuario = float(input("Ingrese su peso en kg: "))
# altura_usuario = float(input("Ingrese su altura en metros: "))

# imc = peso_usuario / (altura_usuario ** 2)

# print(f"Su IMC índice de masa corporal es de: {imc:.2f}")

#Operadores de comparación: 8
#Verificador de edades
# edad_usuario = int(input("Ingrese su edad: "))

# if edad_usuario >= 65:
#     resultado = "Eres mayor de edad."
# elif edad_usuario >= 18:
#     resultado = "Eres adulto."
# else:
#     resultado = "Eres menor de edad."

# print(resultado)

#Operadores lógicos: 9
#Sistema de validación de contraseñas
# def validar_contraseña(contraseña):

#     if len(contraseña) < 8:
#         return False
    
#     tiene_mayuscula = False
#     tiene_minuscula = False
#     for caracter in contraseña:
#         if caracter.isupper():
#             tiene_mayuscula = True
#         elif caracter.islower():
#             tiene_minuscula = True

#     if not tiene_mayuscula or not tiene_minuscula:
#         return False
    
#     tiene_numero = any(caracter.isdigit() for caracter in contraseña)

#     if not tiene_numero:
#         return False
    


#     return True

# contraseña = input("Ingrese su contraseña a validar: ")
# if validar_contraseña(contraseña):
#     print("La contraseña cumple con el protocolo básico de seguridad.")
# else:
#     print("La contraseña no es válida, es insegura.")

#Declaraciones If: 10
#Asistente de clima
# clima_usuario = int(input("Ingrese la temperatura actual: "))

# if clima_usuario >= 30:
#     print("Hace calor.")
# elif clima_usuario >= 20:
#     print("El clima es agradable.")
# else:
#     print("Hace frío.")

#Bucles While: 11
#Juego de adivinanza de números
# import random

# def juego_de_adivinanza():
#     numero_secreto = random.randint(0, 100)
#     intentos = 0

#     while True:
#         intento = int(input("Intente adivinar el número secreto del 1 al 100: "))
#         intentos += 1

#         if intento < numero_secreto:
#             print("El número secreto es mayor al ingresado.")
#         elif intento > numero_secreto:
#             print("El número secreto es menor al ingresado.")
#         else:
#             print(f"Felicidades adivinazte el número secreto: {numero_secreto} en {intentos} intentos!.")
#             break

# juego_de_adivinanza()

#Listas: 12
#Lista de tareas
# tareas = []

# def menu():
#     print("\nOpciones:")
#     print("1. Agregar tarea.")
#     print("2. Eliminar tarea.")
#     print("3. Ver tareas.")
#     print("4. Salir.")

# def agregar_tarea():
#     tarea = input("Ingrese su nueva tarea: ")
#     tareas.append(tarea)
#     print(f"Nueva tarea '{tarea}' añadida.")

# def eliminar_tarea():
#     tarea = input("Ingrese la tarea a eliminar: ")
    
#     if tarea in tareas:
#         tareas.remove(tarea)
#         print(f"Se removio la tarea '{tarea}'.")
#     else:
#         print("No se encuentra la tarea que desea eliminar.")

# def ver_tareas():
#     if not tareas:
#         print("No se encuentran tareas pendientes.")
#     else:
#         print("Tareas pendientes:")
#         for tarea in tareas:
#             print(f"- {tarea}")

# while True: 
#     menu()
#     choise = input("Seleccione una opción: ")

#     if choise == '1':
#         agregar_tarea()
#     elif choise == '2':
#         eliminar_tarea()
#     elif choise == '3':
#         ver_tareas()
#     elif choise == '4':
#         print("Cerrando programa...")
#         break
#     else:
#         print("Opción no válida.")

#Métodos de lista: 13
#Sistema de inventario
# inventario = []

# def mostrar_inventario():
#     print("Inventario actual:")
#     for producto in inventario:
#         print(producto)

# while True:

#     print("\nOpciones:")
#     print("1. Agregar producto.")
#     print("2. Insertar producto en una posición específica.")
#     print("3. Eliminar producto.")
#     print("4. Limpiar inventario.")
#     print("5. Verificar existencia de un producto.")
#     print("6. Contar productos en el inventario.")
#     print("7. Salir.")

#     opcion = input("Elija una opción: ")

#     if opcion == '1':
#         producto = input("Ingrese el nombre del producto a ingresar: ")
#         inventario.append(producto)
    
#     elif opcion == '2':
#         producto = input("Ingrese el producto a insertar: ")
#         posicion = int(input("Ingrese la posición de insertación: "))
#         inventario.insert(posicion, producto)

#     elif opcion == '3':
#         producto_a_eliminar = input("Ingrese el producto a eliminar: ")
#         if producto_a_eliminar in inventario:
#             inventario.remove(producto_a_eliminar)
#         else:
#             print("El producto que desea eliminar no existe.")

#     elif opcion == '4':
#         inventario.clear()
#         print("Inventario limpiado.")
        
#     elif opcion == '5':
#         verificar = input("Ingrese el producto a verificar: ")
#         if not verificar in inventario:
#             print("No existe el producto ingresado.")
#         else:
#             print("Si existe el producto ingresado.")

#     elif opcion == '6':
#         print(f"Cantidad de productos en el inventario: {len(inventario)}.")

#     elif opcion == '7':
#         print("Cerrando programa...")
#         break

#     mostrar_inventario()

#Bucles for: 14
#Generador de tablas de multiplicar
# for i in range(1, 11):
#     print(f"Tabla de multiplicar del {i}:")

#     for j in range(1, 11):
#         producto = i * j
#         print(f"{i} * {j} = {producto}")

#     print()

#La función range(): 15
#Generador de patrones de números
# def mostrar_patron(patron):
#     for numero in patron:
#         print(numero, end=" ")
#     print()

# while True:

#     print("Opciones de patrones:")
#     print("1. Números ascendentes.")
#     print("2. Números descendentes.")
#     print("3. Números pares.")
#     print("4. Números impares.")
#     print("5. Múltiplos de un número específico.")
#     print("6. Salir.")

#     opcion = input("Selecciona una opción: ")

#     if opcion == "1":
#         inicio = int(input("Ingrese el número inicial: "))
#         final = int(input("Ingrese el número final: "))
#         patron = range(inicio, final + 1)
#         mostrar_patron(patron)
#     elif opcion == "2":
#         inicio = int(input("Ingrese el número inicial: "))
#         final = int(input("Ingrese el número final: "))
#         patron = range(inicio, final - 1, - 1)
#         mostrar_patron(patron)
#     elif opcion == "3":
#         inicio = int(input("Ingrese el número inicial(par): "))
#         final = int(input("Ingrese el número final: "))
#         if inicio % 2 != 0:
#             inicio += 1
#         patron = range(inicio, final + 1, 2)
#         mostrar_patron(patron)
#     elif opcion == "4":
#         inicio = int(input("Ingrese el número inicial(impar): "))
#         final = int(input("Ingrese el número final: "))
#         if inicio % 2 == 0:
#             inicio += 1
#         patron = range(inicio, final + 1, 2)
#         mostrar_patron(patron)
#     elif opcion == "5":
#         multiplo = int(input("Ingrese el número multiplo: "))
#         inicio = int(input("Ingrese el número inicial: "))
#         final = int(input("Ingrese el número final: "))
#         patron = range(inicio, final + 1, multiplo)
#         mostrar_patron(patron)
#     elif opcion == "6":
#         break
#     else:
#         print("Opción no válida.")

#Tuplas: 16
#Historial de precios
# historial_precios = []

# def agregar_precio(fecha, precio):
#     historial_precios.append((fecha, precio))

# def precio_maximo():
#     return max(historial_precios, key=lambda x: x[1])

# def precio_minimo():
#     return min(historial_precios, key=lambda x: x[1])

# agregar_precio("2024-06-01", 100.0)
# agregar_precio("2024-06-05", 150.0)
# agregar_precio("2024-06-10", 90.0)

# print("Precio maximo:", precio_maximo())
# print("Precio minimo:", precio_minimo())

#Diccionarios: 17
#Agenda de contactos
# agenda = {}

# def agregar_contacto():
#     nombre = input("Ingrese el nombre del contacto: ")
#     telefono = input("Ingrese el teléfono del contacto: ")
#     direccion = input("Ingrese la dirección del contacto: ")

#     agenda[nombre] = {
#         "teléfono": telefono,
#         "dirección": direccion
#     }

#     print(f"Contacto {nombre} agregado.")

# def buscar_contacto():
#     nombre_contacto = input("Ingrese el nombre del contacto que desee buscar: ")
#     if nombre_contacto in agenda:
#         print(f"Detalles de {nombre_contacto}:")
#         print(f"Teléfono: {agenda[nombre_contacto]['teléfono']}")
#         print(f"Dirección: {agenda[nombre_contacto]['dirección']}")
#     else:
#         print(f"Contacto {nombre_contacto} no encontrado.")

# def eliminar_contacto():
#     nombre = input("Ingrese el nombre del contacto que desee eliminar: ")
#     if nombre in agenda:
#         del agenda[nombre]
#         print(f"Contacto {nombre} eliminado.")
#     else:
#         print(f"Contacto {nombre} inexistente.")

# def mostrar_contactos():
#     if not agenda:
#         print("La agenda está vacía.")
#     else:
#         for nombre, detalles in agenda.items():
#             print(f"Nombre: {nombre}")
#             print(f"Teléfono: {detalles['teléfono']}")
#             print(f"Dirección: {detalles['dirección']}")
#             print()
           
# while True:
#     print("¡Bienvenido a la agenda!")
#     print("Opciones:")
#     print("1. Agregar contacto.")
#     print("2. Buscar contacto.")
#     print("3. Eliminar contacto.")
#     print("4. Mostrar contactos.")
#     print("5. Salir de la agenda.")

#     Seleccion = input("Seleccione una opción: ")

#     if Seleccion == "1":
#         agregar_contacto()
#     elif Seleccion == "2":
#         buscar_contacto()
#     elif Seleccion == "3":
#         eliminar_contacto()
#     elif Seleccion == "4":
#         mostrar_contactos()
#     elif Seleccion == "5":
#         print("Saliendo de la agenda...")
#         print("Ha salido de la agenda.")
#         break
#     else:
#         print("Selección no válida.")

#Excepciones: 18
#Calculadora con manejo de errores
# def calculadora():
#     while True:
#         try:
#             operacion = input("Elija la operación que desee realizar (+, -, *, /) o salir: ")

#             if operacion.lower() == "salir":
#                 print("Salio del programa.")
#                 break

#             num1 = float(input("Ingrese el primer número: "))
#             num2 = float(input("Ingrese el segundo número: "))

#             if operacion == "+":
#                 resultado = num1 + num2
#             elif operacion == "-":
#                 resultado = num1 - num2
#             elif operacion == "*":
#                 resultado = num1 * num2
#             elif operacion == "/":
#                 if num2 == 0:
#                     print("Error: No se puede dividir por 0.")
#                     continue
#                 resultado == num1 / num2
#             else:
#                 print("Operación no válida. Intente nuevamente.")
#                 continue

#             print(f"Resultado: {num1} {operacion} {num2} = {resultado}")

#         except ValueError:
#             print("Error: Ingrese un valor válido.")
#         except ZeroDivisionError:
#             print("Error: No se puede dividir por 0.")
#         except Exception as e:
#             print(f"Error: Error inesperado {e}")

# calculadora()

#Funciones: 19
#Calculadora modular
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def Calculadora():
    while True:
        try:
            print("Seleccione la operación a realizar:")
            print("1. Suma.")
            print("2. Resta.")
            print("3. Multiplicación.")
            print("4. División.")
            print("5. Salir.")

            operacion = input("Del 1 al 5: ")

            if operacion == "5":
                print("Has salido del programa.")
                break

            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if operacion == "1":
                resultado = suma(num1, num2)
                print(f"Resultado: {num1} {operacion} {num2} = {resultado}")
            elif operacion == "2":
                resultado = resta(num1, num2)
                print(f"Resultado: {num1} {operacion} {num2} = {resultado}")
            elif operacion == "3":
                resultado = multiplicacion(num1, num2)
                print(f"Resultado: {num1} {operacion} {num2} = {resultado}")
            elif operacion == "4":
                resultado = division(num1, num2)
                print(f"Resultado: {num1} {operacion} {num2} = {resultado}")
            else:
                print("Opción no válida.")
                continue

        except ZeroDivisionError:
            print("Error: No se puede dividir por 0.")
            continue

if __name__ == "__main__":
    Calculadora()