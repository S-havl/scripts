#Un Array o Matriz es como una lista pero que almacenan un solo tipo de datos al contrario de la listas, que almacenan cualquier tipo de datos.
#Importar modulo Array
import array

# #Segunda manera
import array as arr

# #Tercera manera
from array import *

# #Crear array
Mi_matriz = array.array()

# #Segunda forma
Mi_matriz_2 = arr.array()

# #Tercera forma
Mi_matriz_3 = array()

#Ejemplo
from array import *

Matriz = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(Matriz)
print(Matriz[0:5])

for number in Matriz:
    print(number)

Matriz_float = array('d', [10.0, 20.0, 30.0])
print(Matriz_float)
#Las matrices al ser parecidas a las listas, tienen los mismos metodos, append, remove, pop, etc.

#Otro ejemplos segunda manera de importar el modulo
import array

Mi_Matriz = array.array('i', [1, 2, 3, 4, 5])
print(Mi_Matriz)

#Tercera forma de importar el modulo array
import array as arr

matriz = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
print(matriz)