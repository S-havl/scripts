#Variables: 1
#Inventario de biblioteca
# biblioteca = {}

# def añadir_libro():
#     titulo = input("Ingrese el título del libro: ")
#     autor = input("Ingrese el autor del libro: ")
#     Año_publicacion = input("Ingrese el año de publicación: ")

#     biblioteca[titulo] = {
#         "Autor": autor,
#         "Año de publicación": Año_publicacion
#     }

# def eliminar_libro():
#     nombre_libro = input("Ingrese el libro que desee eliminar: ")
#     if nombre_libro in biblioteca:
#         del biblioteca[nombre_libro]
#         print(f"Libro {nombre_libro} eliminado de la biblioteca.")
#     else:
#         print("El libro que desea eliminar no existe.")

# def mostrar_libros():
#     print("Todos los libros dentro de la biblioteca:")
#     for libro, detalles in biblioteca.items():
#         print(f"Nombre: {libro}")
#         print(f"Autor: {detalles["Autor"]}")
#         print(f"Año de publicación: {detalles["Año de publicación"]}")
#         print()

# def main():
#     while True:
#         print("Bienvenido a la biblioteca:")
#         print("Seleccione una opción:")
#         print("1. Agregar libro.")
#         print("2. Eliminar libro.")
#         print("3. Mostrar libros.")
#         print("4. Salir.")

#         opción = input("Su opción: ")

#         if opción == "1":
#             añadir_libro()
#         elif opción == "2":
#             eliminar_libro()
#         elif opción == "3":
#             mostrar_libros()
#         elif opción == "4":
#             print("Saliste de la biblioteca.")
#             break
#         else:
#             print("Opción no válida.")
#             continue

# if __name__ == "__main__":
#     main()

#Entrada de usuario(input()): 2
#Simulador de encuesta
# Opiniones = []

# def main():
#     print("¡Bienvenido a la encuesta!")
#     print("Escriba su opinión sobre los siguientes temas:")

#     Comida = input("Qué opina sobre la comida?: ")
#     Deporte = input("Qué opinas del deporte?: ")
#     Escuela = input("Qué opinas de la escuela?: ")

#     Opiniones.append(Comida)
#     Opiniones.append(Deporte)
#     Opiniones.append(Escuela)

#     print("Tus opiniones de cada tema:")
#     for Opinion in Opiniones:
#         print(Opinion)

# if __name__ == "__main__":
#     main()

#Conversión de tipos de datos: 3
#Conversor de temperatura
# def Celsius_a_fahrenheit(Celsius):
#     fahrenheit = (Celsius * 9/5) + 32
#     return fahrenheit

# def Celsius_a_Kelvin(Celsius):
#     Kelvin = Celsius + 273.15
#     return Kelvin

# def main():
#     while True:
#         print("Conversor de temperatura.")
#         print("1. Celsius a fahrenheit.")
#         print("2. Celsius a kelvin.")
#         print("3. Salir.")

#         seleccion = input("Elije una opción: ")

#         if seleccion == "1":
#             Celsius = float(input("Ingrese los grados C°: "))
#             fahrenheit = Celsius_a_fahrenheit(Celsius)
#             print(fahrenheit)
#         elif seleccion == "2":
#             Celsius = float(input("Ingrese los grados C°: "))
#             Kelvin = Celsius_a_Kelvin(Celsius)
#             print(Kelvin)
#         elif seleccion == "3":
#             print("Saliste del conversor de temperatura.")
#             break
#         else:
#             print("Selección no válida.")
#             continue

# if __name__ == "__main__":
#     main()

#Operaciones aritméticas: 4
#Calculadora de propinas
# cuenta = float(input("Ingrese la cuenta total: "))
# propina = float(input("Ingrese el porcentaje de propina: "))

# propina_total = (cuenta * propina) / 100

# print(f"Propina a dar: {propina_total}")

#Cadena de caracteres(strings): 5
#Analizador de texto
# def analizar_texto(parrafo):
#     parrafo.lower()
#     palabras = parrafo.split()
#     cantidad_palabras = len(palabras)
#     caracteres = len(parrafo)

#     print(f"Caracteres: {caracteres}")
#     print(f"Cantidad de palabras: {cantidad_palabras}")


# parrafo = input("Ingrese un parrafo de texto: ")
# analizar_texto(parrafo)

#Operadores de comparación: 6
#Verificador de números pares e impares
# def verificar_par_impar():
#     números_usuario = input("Ingrese varios números separados: ")
#     números = números_usuario.split()
#     for numero in números:
#         number = int(numero)
#         if number % 2 == 0:
#             print(f"El número {numero} es par.")
#         else:
#             print(f"El número {numero} es impar.")

# verificar_par_impar()        

#Operadores lógicos: 7
#Sistema de acceso
# def sistema_acceso(usuario, contraseña):
#     data_base = {}

#     data_base["cuenta"] = {
#         "Usuario": "Shavl",
#         "Contraseña": "Iloveyou"
#     }

#     if usuario == data_base["cuenta"]["Usuario"] and contraseña == data_base["cuenta"]["Contraseña"]:
#         print("Acceso concedido.")
#     else:
#         print("Acceso denegado.")
        
# usuario = input("Ingrese su usuario: ")
# contraseña = input("Ingrese su contraseña: ")
# sistema_acceso(usuario, contraseña)

#Declaraciones if: 8
#Calculadora de descuentos
# def calcular_descuento():
#     precio_articulo = float(input("Ingrese el precio del artículo: "))
#     cupon_descuento = input("Tiene cupon de descuento si o no?(S/N): ")

#     if cupon_descuento == "S".lower():
#         cantidad_descuento = float(input("Ingrese el porcentaje del descuento %: "))
#         descuento_aplicado = (precio_articulo * cantidad_descuento) / 100
#         total_pagar = precio_articulo - descuento_aplicado
#         print(f"El descuento es de {descuento_aplicado}.")
#         print(f"Total a pagar con descuento: {total_pagar}")
#     elif cupon_descuento == "N".lower():
#         print("No se le aplica ningún descuento.")
#         print(f"Total a pagar: {precio_articulo}")
#     else:
#         print("Selección inválida.")

# calcular_descuento()

#Bucles while: 9
#Sumador de números
# def sumar_numeros():
#     numeros = []
   
#     while True:
#         print("Opciones:")
#         print("1. Agregar número.")
#         print("2. Mostrar suma total.")
#         print("3. Salir.")
#         print("4. Eliminar todos los números ingresados.")

#         seleccion = input("Seleccione una opción: ")

#         if seleccion == "3":
#             print("Saliste del programa.")
#             break

#         if seleccion == "1":
#             numero = float(input("Ingrese el número a agregar: "))
#             numeros.append(numero)

#         elif seleccion == "2":
#             total = sum(numeros)
#             print(f"La suma total de todos los números ingresados es: {total}")

#         elif seleccion == "4":
#             numeros.clear()
#             print("Números eliminados.")

#         else:
#             print("Selección no válida.")
#             continue

# if __name__ == "__main__":
#     sumar_numeros()

#Listas: 10
#Organizador de viajes
# Viajes = []

# def añadir_viaje():
#     Viaje = input("Ingrese el nombre del viaje: ")
#     destino = input("Ingrese el destino: ")
#     fecha = input("Ingrese la fecha del viaje: ")

#     Viaje = [destino, fecha]

#     Viajes.append(Viaje)
#     print("Viaje añadido.")

# def eliminar_viaje():
#     Destino = input("Ingrese el destino del viaje que desea eliminar: ")
#     Fecha = input("Ingrese la fecha del destino que desea eliminar: ")
    
#     for viaje in Viajes:
#         if Destino.lower() and Fecha.lower() in viaje:
#             Viajes.remove(viaje)
#             print("Viaje eliminado.")

# def mostrar_viajes():
#     print("Viajes añadidos:")
#     for viaje in Viajes:
#         print(viaje)
#         print()

# def main():
#     while True:
#         print("Organizador de viajes:")
#         print("1. Añadir viaje.")
#         print("2. Eliminar viaje.")
#         print("3. Mostrar viajes.")
#         print("4. Salir.")

#         opcion = input("Seleccione una opción: ")

#         if opcion == "1":
#             añadir_viaje()
#         elif opcion == "2":
#             eliminar_viaje()
#         elif opcion == "3":
#             mostrar_viajes()
#         elif opcion == "4":
#             print("Saliste del programa.")
#             break
#         else:
#             print("Opción no válida.")
#             continue

# if __name__ == "__main__":
#     main()

#Métodos de lista: 11
#Gestor de películas
# peliculas = []

# def agregar_pelicula():
#     Nombre = input("Ingrese el nombre de la película: ")
#     peliculas.append(Nombre)
#     print(f"Película {Nombre} añadida.")

# def eliminar_pelicula():
#     Nombre = input("Ingrese el nombre de la película que desea eliminar: ")
#     if Nombre in peliculas:
#         peliculas.remove(Nombre)
#         print(f"Película {Nombre} eliminada.")
#     else:
#         print("Película inexistente.")

# def ver_peliculas():
#     for pelicula in peliculas:
#         print(pelicula)

# def main():
#     while True:
#         print("Gestor de películas")
#         print("1. Agregar película.")
#         print("2. Eliminar película.")
#         print("3. Ver películas.")
#         print("4. Salir del gestor.")

#         seleccion = input("Seleccione una opción: ")

#         if seleccion == "1":
#             agregar_pelicula()
#         elif seleccion == "2":
#             eliminar_pelicula()
#         elif seleccion == "3":
#             ver_peliculas()
#         elif seleccion == "4":
#             print("Saliendo del programa...\nSaliste del programa.")
#             break
#         else:
#             print("Opción no válida.")

# if __name__ == "__main__":
#     main()

#Bucles for: 12
#Calculadora de factorial
# numero = input("Ingrese un número: ")

# factorial = 1

# for i in range(1, int(numero) + 1):
#     factorial *= i

# print(f"El factorial de {numero} es {factorial}")

#Función range(): 13
#Generador de números pares
# def main():
#     while True:
#         rango = int(input("De un rango empezando por cero: "))
#         print("Mostrando pares en el rango de números especificados...")
#         for i in range(1, rango + 1):
#             if i % 2 == 0:
#                 print(i)

#         salir = input("Desea salir del programa?(y/n): ")
#         if salir.lower() == "y":
#             break

# if __name__ == "__main__":
#     main()

#Tuplas: 14
#Gestor de puntos
# puntos = []

# def añadir_coordenadas():
#     x = float(input("Ingrese las cordenadas X: "))
#     y = float(input("Ingrese las cordenada Y: "))
#     z = float(input("Ingrese las cordenadas Z: "))

#     coordenadas = (x, y, z)
#     puntos.append(coordenadas)
#     list_to_tuple = tuple(puntos)
#     print("\nCordenada añadida")
    
# def mostrar_cordenadas():
#     for coordenadas in puntos:
#         print(f"\n{coordenadas}")

# def main():
#     while True:
#         print("Gestor de coordernadas:")
#         print("1. Añadir coordenadas.")
#         print("2. Ver coordenadas guardadas.")
#         print("3. Salir.")

#         seleccion = input("Seleccione una opción: ")

#         if seleccion == "1":
#             añadir_coordenadas()
#         elif seleccion == "2":
#             mostrar_cordenadas()
#         elif seleccion == "3":
#             print("Saliste del programa.")
#             break
#         else:
#             print("Selección no válida.")
#             continue

# if __name__ == "__main__":
#     main()

#Diccionarios: 15
#Inventario de productos
# Productos = {}

# def añadir_producto():
#     nombre = input("Nombre del producto: ")
#     precio = input("Precio del producto: ")

#     Productos[nombre] = precio
#     print("Producto añadido.")

# def eliminar_producto():
#     nombre = input("Nombre del producto a eliminar: ")
#     if nombre.lower() in Productos.keys():
#         del Productos[nombre]
#         print("Producto eliminado.")

# def mostrar_productos():
#     print("\nProductos del inventario:")
#     for clave, valor in Productos.items():
#         print(f"Nombre: {clave}, Precio: {valor}")

# def main():
#     while True:
#         print("Inventario de productos.")
#         print("1. Añadir producto.")
#         print("2. Eliminar producto.")
#         print("3. Mostrar productos.")
#         print("4. Salir del inventario.")

#         opcion = input("Seleccione una opción: ")

#         if opcion == "1":
#             añadir_producto()
#         elif opcion == "2":
#             eliminar_producto()
#         elif opcion == "3":
#             mostrar_productos()
#         elif opcion == "4":
#             print("Saliendo del programa...")
#             print("Saliste del inventario de productos.")
#             break
#         else:
#             print("Seleccione una opción válida.")
#             continue

# if __name__ == "__main__":
#     main()

#Excepciones: 16
#Calculadora segura
# def sumar(n1, n2):
#     return n1 + n2

# def restar(n1, n2):
#     return n1 - n2

# def multiplicar(n1, n2):
#     return n1 * n2

# def dividir(n1, n2):
#     return n1 / n2

# def main():
#     while True:
#         try:
#             print("Calculadora segura:")
#             print("1. Sumar")
#             print("2. Restar")
#             print("3. Múltiplicar")
#             print("4. Dividir")
#             print("5. Salir")

#             seleccion = input("Seleccione una opción: ")

#             if seleccion == "1":
#                 n1 = float(input("Ingrese el primer número: "))
#                 n2 = float(input("Ingrese el segundo número: "))
#                 print(sumar(n1, n2))
#             elif seleccion == "2":
#                 n1 = float(input("Ingrese el primer número: "))
#                 n2 = float(input("Ingrese el segundo número: "))
#                 print(restar(n1, n2))
#             elif seleccion == "3":
#                 n1 = float(input("Ingrese el primer número: "))
#                 n2 = float(input("Ingrese el segundo número: "))
#                 print(multiplicar(n1, n2))
#             elif seleccion == "4":
#                 n1 = float(input("Ingrese el primer número: "))
#                 n2 = float(input("Ingrese el segundo número: "))
#                 print(dividir(n1, n2))
#             elif seleccion == "5":
#                 print("Saliste de la calculadora.")
#                 break
#             else:
#                 print("Seleccione una opción válida.")
#                 continue

#         except ZeroDivisionError:
#             print("Error: división por cero.")
#         except ValueError:
#             print("Error: valor no válido.")

# if __name__ == "__main__":
#     main()

#Funciones:
#Generador de contraseñas:
# import random
# import string

# def generar_contraseña(longitud):
#     caracteres = string.ascii_letters + string.digits + string.punctuation
#     contraseña = ''.join(random.choice(caracteres) for i in range(longitud))

#     return contraseña

# longitud_deseada = int(input("Ingrese la longitud de su contraseña: "))
# contraseña_generada = generar_contraseña(longitud_deseada)
# print(f"Su contraseña generada es: {contraseña_generada}")
    
#Fin.