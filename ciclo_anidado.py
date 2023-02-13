matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz[0][1])  #especificamos primero la lista y luego la otra parte de la lista

for fila in matriz:  #  nos metemos en la lista
    for columna in fila:  #  nos metemos en los elementos de la lista
        print(columna)