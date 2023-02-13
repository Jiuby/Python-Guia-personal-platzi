#crear y leer, actualizar y eliminar datos de una lista
"""
append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
"""

numeros = [1, 2, 3, 4, 5]
print(numeros[1])

#actualizar
numeros[4] = 10
print(numeros)

numeros.append(20)  #lo agrega al final
print(numeros)

numeros.insert(0, "Comienzo")
print(numeros)

numeros.insert(1, 0)
print(numeros)

tareas = ["todo 1", "todo 2", "todo 3"]
lista = numeros + tareas
print(lista)


index = lista.index("todo 2")
lista[index] = "todo 4"
print(lista)

#  remover algo en especifico
lista.remove("todo 1")
print(lista)

#  elimina el ultimo digito
lista.pop()
print(lista)

#  elimina el de la posicion 0
lista.pop(0)
print(lista)

#  voltea todo
lista.reverse()
print(lista)

#  los ordena del menor al mayor
numeros2 = [1, 3, 2, 5, 4, 7, 9]
numeros2.sort()
print(numeros2)

strings = ["cx", "ab", "bd"]
strings.sort()
print(strings)

# no funciona si esta mezclado con numeros y strings
