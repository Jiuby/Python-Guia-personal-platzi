"""
Los elementos están separados por espacios luego de las comas
Los elementos están separados por espacios luego de las comas
Cada posición de la tupla tiene un índice
Es inmutable y por lo tanto no puede ser modificada,
lo que permite proteger mejor la data si no queremos que se modifique por error
"""
numeros = (1, 2, 3, 5)
string = ("juan", "gato", "andres", "juan", "juan")

print(numeros)
print(type(numeros))

print(string)
print(type(string))

#  para saber la posicion usamos lo siguiente
print(numeros[0])
print(numeros[-1])

#  para buscar algo
print(string.index("andres"))

#  contar las veces de un elementos
print(string.count("juan"))

#  convertir de tupla a lista
mi_lista = list(string)
print(mi_lista)
print(type(mi_lista))

mi_lista[1] = "wilson"
print(mi_lista)

#convertir lista a tupla
mi_tupla = tuple(mi_lista)
