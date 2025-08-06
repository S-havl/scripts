#Ejercicio 1: Creación y suma de arrays
# import array

# matriz_1 = array.array('i', [1, 2, 3, 4, 5])
# matriz_2 = array.array('i', [-1, -2, -3, -4, -5])
# suma = matriz_1 + matriz_2
# print(suma)

#Ejercicio 2: Transposición de matriz
# import array as arr

# fila1 = arr.array('i', [1, 2, 3])
# fila2 = arr.array('i', [4, 5, 6])

# matriz = [fila1, fila2]

# transpuesta = [
#     arr.array('i', [matriz[0][0], matriz[1][0]]),
#     arr.array('i', [matriz[0][1], matriz[1][1]]),
#     arr.array('i', [matriz[0][2], matriz[1][2]])
# ]

# for fila in transpuesta:
#     print(fila)

#Ejercicio 3: Suma de dos matrices
# from array import *

# fila1 = array('i', [10, 20])
# fila2 = array('i', [30, 40])

# Matriz_1 = [fila1, fila2]

# fila3 = array('i', [100, 200])
# fila4 = array('i', [300, 400])

# Matriz_2 = [fila3, fila4]

# Matriz_3 = [Matriz_1 + Matriz_2]

# for matriz in Matriz_3:
#     print(matriz)

#Ejercicio 4: Filtrado de elementos
# from array import *

# enteros = array('i', [1, 6, 3, 8, 9, 5, 4, 3, 2, 6, 7, 8])

# valor_filtro = 5

# filtrados = array('i', [num for num in enteros if num > valor_filtro])

# print(f"Número filtrados mayores a", valor_filtro, ":", filtrados)

#Ejercicio 5: Multiplicación de Matriz por escalar
# import array

# fila1 = array.array('i', [1, 2, 3])
# fila2 = array.array('i', [4, 5, 6])
# fila3 = array.array('i', [7, 8, 9])

# matriz = [fila1, fila2, fila3]

# escalar = 3

# matriz_escalada = [array.array('i', [elemento * escalar for elemento in fila]) for fila in matriz]

# print("Matriz escalada 3x3:")
# for fila in matriz_escalada:
#     print(fila)

#Ejercicio 6: Producto de dos matrices
# import array

# matriz1 = [array.array('i', [1, 2]), array.array('i', [3, 4])]
# matriz2 = [array.array('i', [5, 6]), array.array('i', [7, 8])]

# producto_matrices = [
#     array.array('i', [
#         matriz1[0][0] * matriz2[0][0] + matriz1[0][1] * matriz2[1][0],
#         matriz1[0][0] * matriz2[0][1] + matriz1[0][1] * matriz2[1][1]
#     ]),
#     array.array('i', [
#         matriz1[1][0] * matriz2[0][0] + matriz1[1][1] * matriz2[1][0],
#         matriz1[1][0] * matriz2[0][1] + matriz1[1][1] * matriz2[1][1]
#     ])

# ]

# print("Producto de las matrices 2x2:")
# for fila in producto_matrices:
#     print(fila)

#Ejercicio 7: Determinante de una Matriz 2x2
# import array

# matriz = [array.array('i', [1, 2]), array.array('i', [3, 4])]

# determinante = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

# print(f"Determinante de la matriz 2x2: {determinante}")

#Ejercicio 8: Suma de elementos de una fila/columna
# import array

# matriz = [
#     array.array('i', [1, 2, 3]),
#     array.array('i', [4, 5, 6]),
#     array.array('i', [7, 8, 9])
# ]

# suma_fila = sum(matriz[1])
# suma_columna = sum(fila[2] for fila in matriz)

# print("Suma de la segunda fila:", suma_fila)
# print("Suma de la tercera columna:", suma_columna)

#Ejercicio 9: Encontrar el elemento máximo y mínimo
# import array

# matriz = [
#     array.array('i', [1, 2, 3, 4]),
#     array.array('i', [5, 6, 7, 8]),
#     array.array('i', [9, 10, 11, 12]),
#     array.array('i', [13, 14, 15, 16])
# ]

# max_elemento = max(max(fila) for fila in matriz)
# min_elemento = min(min(fila) for fila in matriz)

# print("Elemento máximo:", max_elemento)
# print("Elemento mínimo:", min_elemento)

#Ejercicio 10: Suma de las Diagonales
# import array

# matriz = [
#     array.array('i', [1, 2, 3]),
#     array.array('i', [4, 5, 6]),
#     array.array('i', [7, 8, 9])
# ]

# suma_diagonal_principal = sum(matriz[i][i] for i in range(3))
# suma_diagonal_secundaria = sum(matriz[i][2 - i] for i in range(3))

# print("Suma de la diagonal principal:", suma_diagonal_principal)
# print("Suma de la diagonal secundaria:", suma_diagonal_secundaria)

#Ejercicio 11: Rotación de una matriz 90 grados
# import array

# matriz = [
#     array.array('i', [1, 2, 3]),
#     array.array('i', [4, 5, 6]),
#     array.array('i', [7, 8, 9])
# ]

# matriz_rotada = [
#     array.array('i', [matriz[2][0], matriz[1][0], matriz[0][0]]),
#     array.array('i', [matriz[2][1], matriz[1][1], matriz[0][1]]),
#     array.array('i', [matriz[2][2], matriz[1][2], matriz[0][2]])
# ]

# print("Matriz rotada 90 grados:")
# for fila in matriz_rotada:
#     print(fila)

#Ejercicio 12: Verificar simetría
# import array

# matriz = [
#     array.array('i', [1, 2, 3]),
#     array.array('i', [2, 4, 5]),
#     array.array('i', [3, 5, 6])
# ]

# es_simetrica = all(matriz[i][j] == matriz[j][i] for i in range(3) for j in range(3))

# print("La matriz es simétrica:", es_simetrica)

#Ejercicio 13: Matriz identidad
# import array

# matriz_identidad = [
#     array.array('i', [1 if i == j else 0 for j in range(3)]) for i in range(3)
# ]

# print("Matriz identidad 3x3:")
# for fila in matriz_identidad:
#     print(fila)

#Ejercicio 14: Matriz triangular superior
# import array

# matriz = [
#     array.array('i', [1, 2, 3]),
#     array.array('i', [4, 5, 6]),
#     array.array('i', [7, 8, 9])
# ]

# triangular_superior = [
#     array.array('i', [matriz[i][j] if j >= i else 0 for j in range(3)]) for i in range(3)
# ]

# print("Matriz triangular superior 3x3:")
# for fila in triangular_superior:
#     print(fila)

#Ejercicio 15: Intercambio de filas
# import array

# matriz = [
#     array.array('i', [1, 2, 3]),
#     array.array('i', [4, 5, 6]),
#     array.array('i', [7, 8, 9])
# ]

# matriz_intercambiada = matriz[:]
# matriz_intercambiada[0], matriz_intercambiada[2] = matriz_intercambiada[2], matriz_intercambiada[0]

# print("Matriz con filas intercambiadas:")
# for fila in matriz_intercambiada:
#     print(fila)







